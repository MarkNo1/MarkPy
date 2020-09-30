from .bag_interface import IBag
from server_backup.threads import WorkerConsumer
from pathlib import Path

class BagWriter(IBag, WorkerConsumer):
    def __init__(self,  bag_path, channel, logger):
        Path(bag_path).parent.mkdir(parents=True, exist_ok=True)
        IBag.__init__(self, bag_path,'w', logger)
        WorkerConsumer.__init__(self, channel, logger)
        self.name = '[BagWriter]'


    def add(self, topic, msg, t):
        self.bag.write(topic, msg, t)

    def init(self):
        self.__open__()

    def task(self, val):
        self.add(*val)

    def cleanup(self):
        self.bag.reindex()
        self.bag.flush()
        self.bag.close()
        self.logger(debug=f'{self.name}: Finish writing {self.path} bagfile.')
