from server_backup.threads import WorkerConsumer
from server_backup.bags import correct_path
from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd
import os


class DimensionWorker(WorkerConsumer):
    def __init__(self, channel, bag_path, logger):
        WorkerConsumer.__init__(self, channel, logger)
        self.name = '[DimensionWorker]'
        self.hdf_file = correct_path('stats-dim-bags.hdf')
        self.hdf_key = bag_path.replace('.bag', '').replace('#', '').replace("_","").replace("-","")
        self.topic_dim = {}

    def init(self):
        self.logger(debug=f"{self.name}: Initialization")

    def task(self, val):
        topic = val[0]
        msg = val[1]
        time = val[2]
        if topic not in self.topic_dim:
            self.topic_dim[topic] = len(msg[1])
        else:
            self.topic_dim[topic] += len(msg[1])

    def cleanup(self):
        self.produce_stats()

    def produce_stats(self):
        df = pd.DataFrame(self.topic_dim, index=['Topic', 'Dimension'])
        if os.path.exists(self.hdf_file):
            mode = 'a'
            self.logger(debug=f"{self.name}: Appending statistics in {self.hdf_file} with key: {self.hdf_key}")
        else:
            mode = 'w'
            self.logger(debug=f"{self.name}: Creating statistics file {self.hdf_file} with key: {self.hdf_key}")
        df.to_hdf(self.hdf_file, key=self.hdf_key, mode=mode)



class PlotWorkerDimension:
    def __init__(self, logger):
        self.hfd_file = correct_path('stats-dim-bags.hdf')
        self.logger = logger
        self.name = '[PlotWorkerDimension]'
        self.logger(debug=f"{self.name}: Initialization")
        with pd.HDFStore(self.hfd_file) as hdf:
            self.hdf_keys = hdf.keys()
            for key in self.hdf_keys:
                self.logger(debug=f"{self.name}: Located hdf key: {key}")


    def produce_plots(self):
        for key in self.hdf_keys:
            df = pd.read_hdf(self.hfd_file, key=key)
            df = df.T
            df = df.drop(['Topic'], axis=1)
            df = df['Dimension'] / 1024 / 1024
            out_type = 'pdf'
            plot_folder =  Path(key).parent / 'plots'
            self.logger(debug=f"{self.name}: Creating folder: {plot_folder}")
            plot_folder.mkdir(parents=True, exist_ok=True)
            plot_path = plot_folder / Path(key).name
            self.logger(debug=f"{self.name}: Generating Plot : {plot_path}_dimension.pdf")
            df.plot.bar()
            plt.savefig(str(plot_path) + '_dimension.' + out_type, format=out_type, bbox_inches='tight')
            plt.clf()
            self.logger(debug=f"{self.name}: Plot completed")
            with open(f'{plot_path}.info', 'w') as fd:
                fd.write("MIN\n" + str(df.min(axis=0)))
                fd.write("\n\nMAX\n" + str(df.max(axis=0)))
                fd.write("\n\nMEAN\n" + str(df.mean(axis=0)))
            self.logger(debug=f"{self.name}: Stats min, max and mean created: {plot_path}.info")
