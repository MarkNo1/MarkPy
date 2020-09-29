from watchdog.events import FileSystemEventHandler, RegexMatchingEventHandler
from watchdog.events import FileMovedEvent, DirMovedEvent
from watchdog.events import FileModifiedEvent, DirModifiedEvent
from watchdog.events import FileCreatedEvent, DirCreatedEvent
from watchdog.events import FileDeletedEvent, DirDeletedEvent
from watchdog.observers import Observer
from pathlib import Path

from .filesystem import File, Folder

class BaseWatcher(RegexMatchingEventHandler):

    watcher_events =   {'file': {'moved':FileMovedEvent,
                                'modified': FileModifiedEvent,
                                'created': FileCreatedEvent,
                                'deleted': FileDeletedEvent},
                        'dir':  {'moved':DirMovedEvent,
                                'modified': DirModifiedEvent,
                                'created': DirCreatedEvent,
                                'deleted': DirDeletedEvent}}


    def __init__(self, path=Path.cwd(), target=None ,recursive=False):
        RegexMatchingEventHandler.__init__(self, regexes=[target],  ignore_regexes=['\*.log'])
        self.observer_thread = Observer()
        self.observer_thread.schedule(self, path=path, recursive=recursive)
        self.observer_thread.start()

    def __del__(self):
        self.observer_thread.stop()
        self.observer_thread.join()

    def dispatch(self, event):
        pass


class WatchFile(File, BaseWatcher):

    __watch_file_version = 2

    def __init__(self, fileName, path=Path.cwd(), recursive=False):
        File.__init__(self, fileName, path)
        BaseWatcher.__init__(self, path, target=fileName, recursive=recursive)
        self.newLogAtom('WatchFile', self.__watch_file_version)
        self.initialized()

    def use_event(self, event):
        if event.src_path == str(self.__file__):
            return True
        return False


class WatchFolder(Folder, BaseWatcher):

    __watch_file_version = 2

    def __init__(self, folderName='./', path=Path.cwd(), recursive=False):
        Folder.__init__(self, folderName, path)
        BaseWatcher.__init__(self, path)
        self.newLogAtom('WatchFile', self.__watch_file_version)
        self.initialized()
