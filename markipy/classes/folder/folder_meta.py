from dataclasses import dataclass

from ..path import Path
from ..base import safe_init_meta_class


@dataclass(init=False, unsafe_hash=True)
class FolderMeta:
    _folder_path: Path = None
    _folder_auto_make: bool = False

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
