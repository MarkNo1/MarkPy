from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from multiprocessing import Manager

from ..communication import Communication
from ..base import safe_init_meta


@dataclass(init=False, unsafe_hash=True)
class ProcessMeta(metaclass=ABCMeta):
    _process_name: str = 'Process'
    _process_completed: bool = False

    def __init__(self, **kwargs):
        safe_init_meta(self, kwargs)

    @abstractmethod
    def _process_init(self):
        pass

    @abstractmethod
    def _process_task(self, obj: object = None):
        pass

    @abstractmethod
    def _process_cleanup(self):
        pass
