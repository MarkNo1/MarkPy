from dataclasses import dataclass
import multiprocessing

from .process_meta import ProcessMeta
from ..logger import Logger


@dataclass(init=False, unsafe_hash=True)
class Process(Logger, ProcessMeta, multiprocessing.Process):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        ProcessMeta.__init__(self, **kwargs)
        multiprocessing.Process.__init__(self)

    def run(self):
        self._process_init()
        self._process_task()
        self._process_cleanup()
        self.set_process_completed()

    def set_process_completed(self):
        self._process_completed = True
