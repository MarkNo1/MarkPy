from dataclasses import dataclass

from ...base import safe_init_meta_class
from ...communication import Communication
from ..watcher import Watcher


@dataclass(unsafe_hash=True, init=False)
class WatcherEventProducer(Watcher):
    _watcher_com_channel: Communication = None
    _watcher_com_block: bool = True
    _watcher_com_block_timeout: int = 7

    def __init__(self, **kwargs):
        Watcher.__init__(self, **kwargs)
        safe_init_meta_class(self, kwargs)

    def event_file_moved(self, event):
        self._watcher_com_channel.send(event)

    def event_file_modified(self, event):
        self._watcher_com_channel.send(event)

    def event_file_created(self, event):
        self._watcher_com_channel.send(event)

    def event_file_deleted(self, event):
        self._watcher_com_channel.send(event)

    def event_dir_moved(self, event):
        self._watcher_com_channel.send(event)

    def event_dir_modified(self, event):
        self._watcher_com_channel.send(event)

    def event_dir_created(self, event):
        self._watcher_com_channel.send(event)

    def event_dir_deleted(self, event):
        self._watcher_com_channel.send(event)
