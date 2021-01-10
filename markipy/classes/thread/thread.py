import threading
from dataclasses import dataclass

from .thread_meta import ThreadMeta
from .thread_interface import ThreadInterface

from ..logger import Logger


@dataclass(init=False, unsafe_hash=True)
class Thread(Logger, ThreadMeta, ThreadInterface, threading.Thread):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        ThreadMeta.__init__(self, **kwargs)
        ThreadInterface.__init__(self)
        threading.Thread.__init__(self)

        self.setDaemon(self._thread_daemon)

    def run(self):
        self._thread_init()
        self._thread_task()
        self._thread_cleanup()
        self.set_thread_completed()

    def set_thread_completed(self):
        self._thread_completed = True
