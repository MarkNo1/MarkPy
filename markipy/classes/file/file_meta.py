from dataclasses import dataclass

from ..path import Path
from ..base import safe_init_meta_class


@dataclass(init=False, unsafe_hash=True)
class FileMeta:
    _file_path: Path = None
    _file: object = None

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
