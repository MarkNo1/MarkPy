from dataclasses import dataclass
from os import makedirs

from ..path import Path
from ..logger import Logger

from .folder_meta import FolderMeta
from .folder_exceptions import FolderException


@dataclass(init=False, unsafe_hash=True)
class Folder(Logger, FolderMeta):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        FolderMeta.__init__(self, **kwargs)

        if isinstance(self._folder_path, str):
            self._folder_path = Path(self._folder_path)

        if self._folder_path.is_file():
            raise FolderException.AttachToFile(self)

        if self._folder_auto_make:
            self.make()

    def make(self, exist_ok=True):
        if not self._folder_path.exists():
            makedirs(self._folder_path, exist_ok=exist_ok)
