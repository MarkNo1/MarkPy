from watchdog.events import FileSystemEventHandler
from watchdog.events import FileMovedEvent, DirMovedEvent
from watchdog.events import FileModifiedEvent, DirModifiedEvent
from watchdog.events import FileCreatedEvent, DirCreatedEvent
from watchdog.events import FileDeletedEvent, DirDeletedEvent
from watchdog.observers import Observer
from pathlib import Path

from .logger import Logger, Performance
from .filesystem import File, Folder


class BaseWatcher(Logger, FileSystemEventHandler):
    watcher_events = {'file': {'moved': FileMovedEvent,
                               'modified': FileModifiedEvent,
                               'created': FileCreatedEvent,
                               'deleted': FileDeletedEvent},
                      'dir': {'moved': DirMovedEvent,
                              'modified': DirModifiedEvent,
                              'created': DirCreatedEvent,
                              'deleted': DirDeletedEvent}}

    def __init__(self, path=Path.cwd(), filter_in=[], filter_out=[], recursive=False):
        FileSystemEventHandler.__init__(self)
        Logger.__init__(self)
        self.filter_in = filter_in
        self.filter_out = filter_out
        self.observer_thread = Observer()
        self.observer_thread.schedule(self, path=str(path), recursive=recursive)
        self.observer_thread.start()

    def __del__(self):
        self.observer_thread.stop()
        self.observer_thread.join()

    def _filters(self, event):
        for f_out in self.filter_out:
            if f_out in event.src_path:
                return False
        if event.src_path in self.filter_in:
            return True

    def dispatch(self, event):
        if self._filters(event):
            if isinstance(event, self.watcher_events['file']['moved']):
                self._on_file_moved(event)
            if isinstance(event, self.watcher_events['file']['modified']):
                self._on_file_modified(event)
            if isinstance(event, self.watcher_events['file']['created']):
                self._on_file_created(event)
            if isinstance(event, self.watcher_events['file']['deleted']):
                self._on_file_deleted(event)
            if isinstance(event, self.watcher_events['dir']['moved']):
                self._on_dir_moved(event)
            if isinstance(event, self.watcher_events['dir']['modified']):
                self._on_dir_modified(event)
            if isinstance(event, self.watcher_events['dir']['created']):
                self._on_dir_created(event)
            if isinstance(event, self.watcher_events['dir']['deleted']):
                self._on_dir_deleted(event)

    def _on_file_moved(self, event):
        self.log.debug(f'File moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')

    def _on_file_modified(self, event):
        self.log.debug(f'File modified {self.orange(event.src_path)}')

    def _on_file_created(self, event):
        self.log.debug(f'File created {self.green(event.src_path_)}')

    def _on_file_deleted(self, event):
        self.log.debug(f'File deleted {self.red(event.src_path_)}')

    def _on_dir_moved(self, event):
        self.log.debug(f'Folder moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')

    def _on_dir_modified(self, event):
        self.log.debug(f'Folder modified {self.orange(event.src_path)}')

    def _on_dir_created(self, event):
        self.log.debug(f'Folder created {self.green(event.src_path_)}')

    def _on_dir_deleted(self, event):
        self.log.debug(f'Folder deleted {self.red(event.src_path_)}')


class WatchFile(File, BaseWatcher):
    __watch_file_version__ = 2

    def __init__(self, filePath, recursive=False):
        BaseWatcher.__init__(self, Path(filePath).parent, recursive=recursive)
        File.__init__(self, filePath)
        self.newLogAtom('WatchFile', self.__watch_file_version__)
        self.log.debug(self.ugrey(f'Initialized'))


class WatchFolder(Folder, BaseWatcher):
    __watch_file_version = 2

    def __init__(self, folderPath = Path.cwd(), recursive=False):
        BaseWatcher.__init__(self, Path(folderPath))
        Folder.__init__(self, Path(folderPath))
        self.newLogAtom('WatchFolder', self.__watch_file_version)
        self.log.debug(self.ugrey(f'Initialized'))
