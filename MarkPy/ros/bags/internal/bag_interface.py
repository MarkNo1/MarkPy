import rosbag
from rospy import set_param
from pathlib import Path
from tqdm import tqdm

from MarkPy.basic import Logger, File

class IBag(Logger):
    '''
        Interface Bag Wrapper.
    '''

    def __init__(self, bag_path,  mode, path=Path.cwd()):
        Logger.__init__(self, f'.bag_{bag_path}.log', path=path)
        self.newLogAtom('IBag', self.__process_version__)
        set_param('use_sim_time', True)
        self.bagFile = File(bag_path)
        self.bag = None
        self.end = None
        self.len = None
        self.mode = mode
        self.initialized()

    def __open__(self):
        log_mode = 'read' if 'r' in self.mode else 'write'
        self.log.debug('Opening {self.bagFile} in {log_mode} mode.')

        self.bag = rosbag.Bag(self.bagFile, self.mode, allow_unindexed=True)
        if self.mode == 'r':
            self.end = self.bag.get_end_time()

    def __len__(self):
        return self.len

    def __call__(self, **kargs):
        for topic, msg, t in tqdm(self.bag.read_messages(kargs), total=self.len, dynamic_ncols=True):
            yield topic, msg, t

    def raw(self):
        for topic, msg, t in tqdm(self.bag.read_messages(raw=True), total=self.len, dynamic_ncols=True):
            yield topic, msg, t
