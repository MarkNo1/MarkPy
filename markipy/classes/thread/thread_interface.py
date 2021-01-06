from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass(unsafe_hash=True, init=False)
class ThreadInterface(metaclass=ABCMeta):

    @abstractmethod
    def _thread_init(self):
        pass

    @abstractmethod
    def _thread_task(self, obj: object = None):
        pass

    @abstractmethod
    def _thread_cleanup(self):
        pass
