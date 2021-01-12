from dataclasses import dataclass

from ..logger import Logger
from .thread_abc import ThreadABC


@dataclass(init=False, unsafe_hash=True)
class Thread(Logger, ThreadABC):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        ThreadABC.__init__(self, **kwargs)

        self.setDaemon(self._thread_daemon)

    def run(self):
        self._thread_init()
        self._thread_task()
        self._thread_cleanup()
        self.set_thread_completed()

    def set_thread_completed(self):
        self._thread_completed = True
