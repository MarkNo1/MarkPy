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
    _base_watcher_version = 2

    def __init__(self, logname='BaseWatcher', path=Path.cwd(), target=None, recursive=False):
        FileSystemEventHandler.__init__(self)
        Logger.__init__(self, logname)
        self.newLogAtom('BaseWatcher', self._base_watcher_version)

        look = Path(path).strip()

        self.target = target
        self.observer_thread = Observer()
        self.observer_thread.schedule(self, path=look, recursive=recursive)
        self.observer_thread.start()

        self.log.debug(f'Filesystem observer point to: {self.cyan(look)}')

    def __del__(self):
        self.observer_thread.stop()
        self.observer_thread.join()

    def _check_target(self, event):
        if self.target:
            if event.src_path == self.target:
                return True
        else:
            return True
        return False

    def dispatch(self, event):
        print(event)
        if self._check_target(event):
            if isinstance(event, FileMovedEvent):
                self.on_file_moved(event)
            if isinstance(event, FileModifiedEvent):
                self.on_file_modified(event)
            if isinstance(event, FileCreatedEvent):
                self.on_file_created(event)
            if isinstance(event, FileDeletedEvent):
                self.on_file_deleted(event)
            if isinstance(event, DirMovedEvent):
                self.on_dir_moved(event)
            if isinstance(event, DirModifiedEvent):
                self.on_dir_modified(event)
            if isinstance(event, DirCreatedEvent):
                self.on_dir_created(event)
            if isinstance(event, DirDeletedEvent):
                self.on_dir_deleted(event)

    def on_file_moved(self, event):
        self.log.debug(f'File moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')

    def on_file_modified(self, event):
        self.log.debug(f'File modified {self.orange(event.src_path)}')

    def on_file_created(self, event):
        self.log.debug(f'File created {self.green(event.src_path)}')

    def on_file_deleted(self, event):
        self.log.debug(f'File deleted {self.red(event.src_path)}')

    def on_dir_moved(self, event):
        self.log.debug(f'Folder moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')

    def on_dir_modified(self, event):
        self.log.debug(f'Folder modified {self.orange(event.src_path)}')

    def on_dir_created(self, event):
        self.log.debug(f'Folder created {self.green(event.src_path)}')

    def _on_dir_deleted(self, event):
        self.log.debug(f'Folder deleted {self.red(event.src_path)}')


class WatchFile(File, BaseWatcher):
    __watch_file_version__ = 2

    def __init__(self, filePath, recursive=False):
        BaseWatcher.__init__(self, 'WatchFile', Path(filePath).parent, target=Path(filePath), recursive=recursive)
        File.__init__(self, filePath)
        self.newLogAtom('WatchFile', self.__watch_file_version__)
        self.log.debug(self.ugrey(f'Initialized'))


class WatchFolder(Folder, BaseWatcher):
    __watch_file_version = 2

    def __init__(self, folderPath=Path.cwd(), recursive=False):
        BaseWatcher.__init__(self, 'WatchFolder', Path(folderPath), recursive=recursive)
        Folder.__init__(self, Path(folderPath))
        self.newLogAtom('WatchFolder', self.__watch_file_version)
        self.log.debug(self.ugrey(f'Initialized'))
