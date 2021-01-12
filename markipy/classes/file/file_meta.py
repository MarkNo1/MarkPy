from dataclasses import dataclass
from enum import Enum

from ..path import Path
from ..base import safe_init_meta


@dataclass(init=False, unsafe_hash=True)
class FileMeta:

    _file_name: str = 'FileMeta.Temp'

    class FileMode(Enum):
        read = 'r'
        write = 'w'
        read_write = 'w+'
        append = 'a'
        read_append = 'a+'

    _file_path: Path = None
    _file: object = None
    _file_mode: FileMode = FileMode.read
    _is_file_open: bool = False
    _file_default_open: bool = False

    def __init__(self, **kwargs):
        safe_init_meta(self, kwargs)
