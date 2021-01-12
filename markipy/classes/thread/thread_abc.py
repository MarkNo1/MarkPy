from dataclasses import dataclass
import threading

from abc import ABCMeta, abstractmethod

from ..communication import Communication
from ..communication.channels.int import MessageQueue
from ..base import safe_init_meta


@dataclass(unsafe_hash=True, init=False)
class ThreadABC(threading.Thread, metaclass=ABCMeta):
    _thread_name: str = 'ThreadABCDefault'
    _thread_daemon: bool = True

    _thread_com_channel: Communication = None
    _thread_com_def_factory: MessageQueue = MessageQueue
    _thread_com_block: bool = True
    _thread_com_block_timeout: int = 7

    _thread_completed: bool = False

    @abstractmethod
    def _thread_init(self):
        pass

    @abstractmethod
    def _thread_task(self, obj: object = None):
        pass

    @abstractmethod
    def _thread_cleanup(self):
        pass

    def __init__(self, **kwargs):
        safe_init_meta(self, kwargs)
        threading.Thread.__init__(self)

        if self._thread_com_channel is None:
            self._thread_com_channel = self._thread_com_def_factory(block=self._thread_com_block,
                                                                    timeout=self._thread_com_block_timeout)
