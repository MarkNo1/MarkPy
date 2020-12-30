from dataclasses import dataclass

from ..logger import Logger, has_logger_class
from .communication_interface import CommunicationInterface

COMMUNICATION_DEFAULT_TIME_OUT_SECS = 7


@dataclass(unsafe_hash=True, init=False)
class Communication(CommunicationInterface, Logger):

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        CommunicationInterface.__init__(self, **kwargs)

    def one_publisher_completed(self):
        with self._com_producer_lock:
            self._com_publisher_completed += 1
            if self._com_n_publisher == self._com_publisher_completed:
                self._com_completed = True

    def is_communication_completed(self):
        return self._com_completed

    def send_ack_message_processed(self):
        try:
            return self._com_send_ack_message_processed()
        except Exception as Ex:
            if has_logger_class(self):
                self.log.error(f"Error in send_ack_receive method: {Ex}")
            return None

    def receive(self, block=False, timeout=COMMUNICATION_DEFAULT_TIME_OUT_SECS) -> object:
        try:
            return self._com_receive(block, timeout)
        except Exception as Ex:
            if has_logger_class(self):
                self.log.error(f"Error in receive method: {Ex}")
            return None

    def send(self, var, block=False, timeout=COMMUNICATION_DEFAULT_TIME_OUT_SECS):
        try:
            return self._com_send(var, block, timeout)
        except Exception as Ex:
            if has_logger_class(self):
                self.log.error(f"Error in send method: {Ex}")
            return None

    def get_channel_complete(self):
        return self._com_completed
