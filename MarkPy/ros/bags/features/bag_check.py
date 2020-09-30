from server_backup.bags import correct_path
from server_backup.threads import WorkerConsumer
from matplotlib import pyplot as plt
from pathlib import Path
import pandas as pd
import os



class CheckWorker(WorkerConsumer):
    data = []
    df = None


    def __init__(self, bagfile, channel, logger):
        WorkerConsumer.__init__(self, channel, logger)
        self.name = '[CheckWorker]'
        self.hdf_key = bagfile.replace('.bag', '').replace('#', '').replace("_","").replace("-","")
        self.hdf_file = correct_path('stats-delay-bags.hdf')

    def init(self):
        self.logger(debug=f"{self.name}: Initialization")

    def task(self, val):
        topic = val[0]
        msg = val[1]
        time = val[2]

        if hasattr(msg, 'header'):
            if msg.header.stamp.secs > 0:
                diff = time - msg.header.stamp
                self.data.append(dict(topic=topic, delay=diff.to_nsec()))
            else:
                self.data.append(dict(topic=topic, delay=0))

        elif '/velodyne_packets' == topic:
            diff = time - msg.stamp
            self.data.append(dict(topic=topic, delay=diff.to_nsec()))

        elif '/tf' == topic and msg.transforms:
            diff = time - msg.transforms[0].header.stamp
            self.data.append(dict(topic=topic, delay=diff.to_nsec()))

    def cleanup(self):
        self.df = pd.DataFrame(self.data)
        if os.path.exists(self.hdf_file):
            mode = 'a'
            self.logger(debug=f"{self.name}: Appending statistics to {self.hdf_file} with key: {self.hdf_key}")
        else:
            mode = 'w'
            self.logger(debug=f"{self.name}: Creating statistics to {self.hdf_file} with key: {self.hdf_key}")

        self.df.to_hdf(self.hdf_file, key=self.hdf_key, mode=mode)
        self.logger(debug=f"{self.name}: Done")


class PlotWorker:
    def __init__(self, logger):
        self.hfd_file = correct_path('stats-delay-bags.hdf')
        self.logger = logger
        self.name = '[PlotWorker]'
        with pd.HDFStore(self.hfd_file) as hdf:
            self.hdf_keys = hdf.keys()
            for key in self.hdf_keys:
                self.logger(debug=f"{self.name}: Located hdf key: {key}")


    def produce_plots(self):
        for key in self.hdf_keys:
            plot_folder =  Path(key).parent / 'plots'
            self.logger(debug=f"{self.name}: Creating folder: {plot_folder}")
            plot_folder.mkdir(parents=True, exist_ok=True)
            plot_path = plot_folder / Path(key).name
            self.generate_plots(pd.read_hdf(self.hfd_file, key=key), str(plot_path))


    def convert_to_ms(self,frame):
        frame['delay'] = frame['delay'] * 1e-6
        return frame


    def filter_zero_heading(self,frame):
        return frame[frame['delay'] < 100000 * 1e6]


    def reframe_bycolumn(self,frame):
        series = frame.groupby('topic')['delay'].apply(list)
        max_len = []
        col_name = []
        rows = series.shape[0]
        for r in range(0, rows):
            max_len.append(len(series[r]))
            col_name.append(series.index[r])

        reframe = pd.DataFrame(index=range(max(max_len)), columns=col_name)

        for r in range(0, rows):
            reframe[series.index[r]] = pd.Series(series[r])
        return reframe


    def generate_plots(self, frame, plot_path):
        out_type = 'pdf'
        frame = self.convert_to_ms(frame)
        frame = self.filter_zero_heading(frame)
        reframe = self.reframe_bycolumn(frame)
        self.logger(debug=f"{self.name}: Generating Plot: {plot_path }_delay_complete.pdf")
        reframe.boxplot(vert=False, figsize=(50, 70), fontsize=20)
        plt.subplots_adjust(left=0.25)
        plt.xlim((-0.1, frame['delay'].max()))
        plt.savefig(plot_path + '_delay_complete.' + out_type, dpi=350, format=out_type, bbox_inches='tight')
        plt.clf()
        self.logger(debug=f"{self.name}: Plot completed")
        self.logger(debug=f"{self.name}: Generating Plot without outliers: {plot_path}_delay_nooutliers.pdf")
        reframe.boxplot(vert=False, figsize=(70, 70), sym='', showfliers=False, fontsize=20)
        plt.subplots_adjust(left=0.25)
        plt.xlim((-0.1, 100))
        plt.savefig(plot_path + '_delay_nooutliers.' + out_type, dpi=350, format=out_type, bbox_inches='tight')
        plt.clf()
        self.logger(debug=f"{self.name}: Plot no outliers completed")

        with open(plot_path+'.info', 'w') as fd:
            fd.write("MIN\n" + str(reframe.min()))
            fd.write("\n\nMAX\n" + str(reframe.max()))
            fd.write("\n\nMEAN\n" + str(reframe.mean()))

        self.logger(debug=f"{self.name}: Stats min, max and mean created: {plot_path}.info")
