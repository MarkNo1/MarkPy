
import rosbag
from rospy import set_param
from pathlib import Path
from tqdm import tqdm

from MarkPy.basic import Logger, File


import asyncio
class Producer:
    def __init__(self):
        self.queue = asyncio.Queue

    async def produce(self):
        for x in range(0, 100):
            await self.queue.put(val)

class Consumer:
    def __init__(self, queue):
        self.queue = queue

    async def consume(self, fx):
        val =  await self.queue.get()
        fx(val)
        self.queue.task_done()


class Bag(Logger):
    '''
        Interface Bag Wrapper.
    '''
    __bag_open__ : bool = False
    end : int = 0
    len : int = 0
    mode: str = 'r'
    bagFile : File = None
    bag : rosbag.Bag = None
    queue : asyncio.Queue = None

    def __init__(self, bag_path,  mode, path=Path.cwd()):
        Logger.__init__(self, f'.bag_{bag_path}.log', path=path)
        self.newLogAtom('IBag', self.__process_version__)
        set_param('use_sim_time', True)
        self.bagFile = File(bag_path)
        self.mode = mode

        if self.mode == 'r':
            self.queue = asyncio.Queue
        try:
            self.len = bag.get_message_count()
        except Exception as e:
            self.log.error(e)


        self.initialized()

    def __open__(self):
        log_mode = 'read' if 'r' in self.mode else 'write'
        self.log.debug('Opening {self.bagFile} in {log_mode} mode.')

        self.bag = rosbag.Bag(self.bagFile, self.mode, allow_unindexed=True)
        if self.mode == 'r':
            self.end = self.bag.get_end_time()
        self.__bag_open__ = True

    def info(self):
        self.log.debug('Requested info')
        if self.__bag_open__:
            return self.bag.get_type_and_topic_info().topics
        else:
            return 'Open the bag first'

    def getQueue(self):
        self.log.debug('Requested queue')
        return self.queue

    def setQueue(self, queue):
        self.log.debug('Attache to queue')
        self.queue = queue


    def __len__(self):
        return self.len

    def read(self):
        assert self.mode == 'r'
        asyncio.run(self._read)

    async def _read(self, **kargs):
        for topic, msg, t in tqdm(self.bag.read_messages(kargs), total=self.len, dynamic_ncols=True):
            await self.queue.put(topic, msg, t)
        await self.queue.join()

    def raw(self):
        assert self.mode == 'r'
        asyncio.run(self._raw)

    async def _raw(self):
        for topic, msg, t in tqdm(self.bag.read_messages(raw=True), total=self.len, dynamic_ncols=True):
            await self.queue.put(topic, msg, t)
        await self.queue.join()

    async def write(self):
        while True:
            topic, msg, t = await self.queue.get()
            self.bag.write(topic, msg, t)
            self.queue.task_done()
