from dataclasses import dataclass
from abc import ABCMeta, abstractmethod

from .file_meta import FileMeta


@dataclass(init=False, unsafe_hash=True)
class FileInterface(FileMeta, metaclass=ABCMeta):

    def __init__(self, **kwargs):
        FileMeta.__init__(self, **kwargs)
        self._file_exception_control()


    def _file_exception_control(self):

        if self._file_path.is_dir():
            raise FileAttacheToFolder(self)



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
