from ..watcher import Watcher

from dataclasses import dataclass


@dataclass(unsafe_hash=True, init=False)
class WatcherLogger(Watcher):

    def event_file_moved(self, event):
        self.log.debug(f'File moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')

    def event_file_modified(self, event):
        self.log.debug(f'File modified {self.orange(event.src_path)}')

    def event_file_created(self, event):
        self.log.debug(f'File created {self.green(event.src_path)}')

    def event_file_deleted(self, event):
        self.log.debug(f'File deleted {self.red(event.src_path)}')

    def event_dir_moved(self, event):
        self.log.debug(f'Folder moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')

    def event_dir_modified(self, event):
        self.log.debug(f'Folder modified {self.orange(event.src_path)}')

    def event_dir_created(self, event):
        self.log.debug(f'Folder created {self.green(event.src_path)}')

    def event_dir_deleted(self, event):
        self.log.debug(f'Folder deleted {self.red(event.src_path)}')
