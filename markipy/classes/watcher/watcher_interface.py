from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass(unsafe_hash=True, init=False)
class WatcherInterface(metaclass=ABCMeta):

    @abstractmethod
    def event_file_moved(self, event):
        pass

    @abstractmethod
    def event_file_modified(self, event):
        pass

    @abstractmethod
    def event_file_created(self, event):
        pass

    @abstractmethod
    def event_file_deleted(self, event):
        pass

    @abstractmethod
    def event_dir_moved(self, event):
        pass

    @abstractmethod
    def event_dir_modified(self, event):
        pass

    @abstractmethod
    def event_dir_created(self, event):
        pass

    @abstractmethod
    def event_dir_deleted(self, event):
        pass
