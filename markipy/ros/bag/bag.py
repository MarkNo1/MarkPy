import rosbag
from tqdm import tqdm

from markipy.basic import Logger
from markipy.basic import ThreadProducer, ThreadConsumer
from markipy.basic import File

_ibag_ = {'class': 'IBag', 'version': 3}
_bag_reader_ = {'class': 'BagReader', 'version': 4}


class IBag(Logger):

    def __init__(self, bagPath, mode):
        Logger.__init__(self, file_log='IBag')
        self._init_atom_register_class(_ibag_)
        self.bagFile = File(bagPath)
        self.mode = mode
        self.end = 0
        self.len = 0
        self.bag = None
        self.__bag_open__ = False

        self.log.debug(self.ugrey(f'Initialized'))

    def __open__(self):
        log_mode = 'read' if 'r' in self.mode else 'write'
        self.log.debug(f'Opening {self.bagFile} in {log_mode} mode.')

        self.bag = rosbag.Bag(str(self.bagFile), self.mode, allow_unindexed=True)
        if self.mode == 'r':
            self.end = self.bag.get_end_time()
            try:
                self.len = self.bag.get_message_count()
            except Exception as e:
                self.log.error(f'Error in bag getting message count: {e}')
        self.__bag_open__ = True

    def info(self):
        self.log.debug('Requested info')
        if self.__bag_open__:
            return self.bag.get_type_and_topic_info().topics
        else:
            return 'Open the bag first'

    def __len__(self):
        return self.len

    def read(self, **kargs):
        assert self.mode == 'r'
        for topic, msg, time in tqdm(self.bag.read_messages(kargs), total=self.len, dynamic_ncols=True):
            yield topic, msg, time

    def raw(self):
        assert self.mode == 'r'
        for topic, msg, time in tqdm(self.bag.read_messages(raw=True), total=self.len, dynamic_ncols=True):
            yield topic, msg, time

    def add(self, topic, msg, time):
        assert self.mode == 'w'
        self.bag.write(topic, msg, time)


class BagReader(IBag, ThreadProducer):
    __bag_reader_version__: str = '3'

    def __init__(self, bag_path, channel):
        IBag.__init__(self, bag_path, 'r')
        ThreadProducer.__init__(self, channel, 'BagReader')
        self._init_atom_register_class(_bag_reader_)

    def init(self):
        self.__open__()

    def task(self):
        try:
            for topic, msg, t in self.read():
                self.produce([topic, msg, t])
            self.set_finish()
        except Exception as e:
            self.log.error(f"Error in task -> {e}")


class BagRawReader(IBag, ThreadProducer):
    __bag_raw_reader_version__: str = '3'

    def __init__(self, bag_path, channel):
        IBag.__init__(self, bag_path, 'r')
        ThreadProducer.__init__(self, channel, 'BagRawReader')
        self.newLogAtom('BagRawReader', self.__bag_raw_reader_version__)
        self.log.debug(self.ugrey(f'Initialized'))

    def init(self):
        self.__open__()

    def task(self):
        for topic, msg, t in self.raw():
            self.produce([topic, msg, t])
        self.set_finish()
        self.log.debug(f'Finish raw reading {self.bagFile}')

    def cleanup(self):
        self.bag.close()


class BagWriter(IBag, ThreadConsumer):
    __bag_writer_version__: str = '3'

    def __init__(self, bag_path, channel):
        IBag.__init__(self, bag_path, mode='w')
        ThreadConsumer.__init__(self, channel, 'BagWriter')
        self.newLogAtom('BagWriter', self.__bag_writer_version__)
        self.log.debug(self.ugrey(f'Initialized'))

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
        self.log.debug(f'Finish writing {self.bagFile}')
