from pathlib import Path

from MarkPy.threads import WorkerProducer
from .bag_interface import IBag



class BagReader(IBag, WorkerProducer):
    def __init__(self,  bag_path, channel, path=Path.cwd()):
        IBag.__init__(self, bag_path, 'r', path)
        WorkerProducer.__init__(self, channel)

    def init(self):
        self.__open__()

    def task(self):
        try:
            for topic, msg, t in self.__call__():
                self.produce([topic, msg, t])
            self.set_finish()
        except Exception as e:
            self.logger(error=f"{self.name}: Error -> {e}")


    def cleanup(self):
        self.logger(debug=f'{self.name}: Finish reading {self.path} bagfile')
        self.bag.close()
        self.logger(debug=f'{self.name}: Bagfile {self.path} closed')


class BagRawReader(IBag, WorkerProducer):
    def __init__(self,  bag_path, channel, logger):
        IBag.__init__(self, bag_path, 'r', logger)
        WorkerProducer.__init__(self, channel, logger)

    def init(self):
        self.__open__()

    def task(self):
        for topic, msg, t in self.raw():
            self.produce([topic, msg, t])
        self.set_finish()
        self.logger(debug=f'{self.name}: Finish raw reading {self.path} bagfile')

    def cleanup(self):
        self.bag.close()
