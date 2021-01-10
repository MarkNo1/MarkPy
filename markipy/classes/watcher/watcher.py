from dataclasses import dataclass
from enum import Enum

from watchdog.events import FileSystemEventHandler
from watchdog.events import FileMovedEvent, DirMovedEvent
from watchdog.events import FileModifiedEvent, DirModifiedEvent
from watchdog.events import FileCreatedEvent, DirCreatedEvent
from watchdog.events import FileDeletedEvent, DirDeletedEvent
from watchdog.observers import Observer

from .watcher_meta import WatcherMeta
from .watcher_interface import WatcherInterface

from ..logger import Logger


@dataclass(init=False, unsafe_hash=True)
class Watcher(Logger, WatcherMeta, WatcherInterface, FileSystemEventHandler):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        WatcherMeta.__init__(self, **kwargs)
        WatcherInterface.__init__(self)
        FileSystemEventHandler.__init__(self)

        # Target File Mode
        if self._watcher_file is not None:
            self._watcher_path = self._watcher_file.parent

    def start(self):
        self._watcher_observer = Observer()
        self._watcher_observer.schedule(self, path=str(self._watcher_path), recursive=self._watcher_recursive)
        self._watcher_observer.start()

    def stop(self):
        self._watcher_observer.stop()
        self._watcher_observer.join()

    def __del__(self):
        self.stop()

    def _watcher_dispatch(self, event):
        if self._watcher_file is not None:
            self._watcher_dispatch_target_file(event)
        else:
            self._watcher_dispatch_folder(event)

    def _watcher_dispatch_target_file(self, event):
        if event.src_path == str(self._watcher_file):
            if isinstance(event, FileMovedEvent):
                self.event_file_moved(event)
            elif isinstance(event, FileModifiedEvent):
                self.event_file_modified(event)
            elif isinstance(event, FileCreatedEvent):
                self.event_file_created(event)
            elif isinstance(event, FileDeletedEvent):
                self.event_file_deleted(event)

    def _watcher_dispatch_folder(self, event):
        if isinstance(event, FileMovedEvent):
            self.event_file_moved(event)
        elif isinstance(event, FileModifiedEvent):
            self.event_file_modified(event)
        elif isinstance(event, FileCreatedEvent):
            self.event_file_created(event)
        elif isinstance(event, FileDeletedEvent):
            self.event_file_deleted(event)
        elif isinstance(event, DirMovedEvent):
            self.event_dir_moved(event)
        elif isinstance(event, DirModifiedEvent):
            self.event_dir_modified(event)
        elif isinstance(event, DirCreatedEvent):
            self.event_dir_created(event)
        elif isinstance(event, DirDeletedEvent):
            self.event_dir_deleted(event)
