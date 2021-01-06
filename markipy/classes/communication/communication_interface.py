from dataclasses import dataclass
from abc import ABCMeta, abstractmethod

from .communication_meta import CommunicationMeta


@dataclass(unsafe_hash=True, init=False)
class CommunicationInterface(CommunicationMeta, metaclass=ABCMeta):

    @abstractmethod
    def _com_receive(self, block, timeout):
        pass

    @abstractmethod
    def _com_send(self, obj, block, timeout):
        pass

    @abstractmethod
    def _com_send_ack_message_processed(self):
        pass

    @abstractmethod
    def wait_completion_buffer(self):
        # Blocks until all items in the queue have been gotten and processed
        pass

    @abstractmethod
    def is_buffer_full(self):
        pass

    @abstractmethod
    def is_buffer_empty(self):
        pass
