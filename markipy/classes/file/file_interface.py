from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass(init=False, unsafe_hash=True)
class FileInterface(metaclass=ABCMeta):

    @abstractmethod
    def _file_attach_init(self) -> bool:
        pass

    @abstractmethod
    def _file_open(self) -> bool:
        pass

    @abstractmethod
    def _file_read(self) -> object:
        return object

    @abstractmethod
    def _file_write(self, var: object):
        pass

    @abstractmethod
    def _file_close(self) -> bool:
        pass

