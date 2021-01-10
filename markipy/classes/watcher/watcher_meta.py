from dataclasses import dataclass

from watchdog.observers import Observer

from ..path import Path
from ..base import safe_init_meta_class


@dataclass(init=False, unsafe_hash=True)
class WatcherMeta:
    _watcher_name: str = 'Watcher'
    _watcher_path: Path = None
    _watcher_file: Path = None
    _watcher_recursive: bool = True
    _watcher_observer: Observer = None

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
