from dataclasses import dataclass

from ..logger import Logger
from .file_interface import FileInterface
from .file_exceptions import FileException
from .file_meta import FileMeta


@dataclass(init=False, unsafe_hash=True)
class File(Logger, FileMeta, FileInterface):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        FileMeta.__init__(self, **kwargs)
        FileInterface.__init__(self)

        self._file_path = self._class_working_path / self._file_name

        self._file_pre_attach_control()
        self.attach()

        if self._file_default_open and not self._is_file_open:
            self.open()

    def _file_pre_attach_control(self):
        if self._file_path.is_dir():
            raise FileException.AttachToFolder(self)
        if self._file_mode is self.FileMode.read and not self._file_path.exists():
            raise FileException.FileDoNotExist(self)

    def attach(self):
        if not self._file_attach_init():
            raise FileException.AttachError(self)

    def open(self):
        if not self._file_open():
            raise FileException.OpenError(self)
        self._is_file_open = True

    def _file_mode_can_read(self):
        if self._file_mode in [
            self.FileMode.read,
            self.FileMode.read_append,
            self.FileMode.read_write
        ]:
            return True
        else:
            return False

    def _file_mode_can_write(self):
        if self._file_mode in [
            self.FileMode.write,
            self.FileMode.read_append,
            self.FileMode.read_write
        ]:
            return True
        else:
            return False

    def read(self):
        if not self._file_mode_can_read():
            raise FileException.ReadModeNotEnabled(self)
        if not self._is_file_open:
            raise FileException.FileNotOpenedYet(self)
        try:
            return self._file_read()
        except Exception as Ex:
            self.log.error(f"Error in read. {Ex}")

    def write(self, var):
        if not self._file_mode_can_write():
            raise FileException.WriteModeNotEnabled(self)
        if not self._is_file_open:
            raise FileException.FileNotOpenedYet(self)
        try:
            return self._file_write(var)
        except Exception as Ex:
            self.log.error(f"Error in write. {Ex}")

    def close(self):
        self._is_file_open = False
        if not self._file_close():
            raise FileException.CloseError(self)

    def get_folder_path(self):
        return self._file_path.parent

    def __del__(self):
        if self._is_file_open:
            self.close()
        super().__del__()
