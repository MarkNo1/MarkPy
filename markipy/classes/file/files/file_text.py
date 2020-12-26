from dataclasses import dataclass
from ..file import File


@dataclass(init=False, unsafe_hash=True)
class TextFile(File):

    _class_name = 'TextFile'

    def _file_attach_init(self) -> bool:
        return True

    def _file_open(self) -> bool:
        self._file = open(self._file_path, self._file_mode.value)
        return True

    def _file_read(self) -> object:
        return self._file.read()

    def _file_write(self, text: str):
        self._file.write(str(text))
        return True

    def _file_close(self) -> bool:
        self._file.close()
        return True
