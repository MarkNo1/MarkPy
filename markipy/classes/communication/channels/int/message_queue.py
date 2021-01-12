from queue import Queue
from dataclasses import dataclass

from ...communication import Communication


@dataclass(unsafe_hash=True, init=False)
class MessageQueue(Communication):
    _com_channel: Queue = None

    def __init__(self, **kwargs):
        Communication.__init__(self, **kwargs)
        self._com_channel = Queue(self._com_buffer_size)

    def _com_receive(self, block, timeout) -> object:
        return self._com_channel.get(block=block, timeout=timeout)

    def _com_send(self, var, block, timeout):
        self._com_channel.put(var, block=block, timeout=timeout)

    def _com_send_ack_message_processed(self):
        self._com_channel.task_done()

    def wait_completion_buffer(self):
        self._com_channel.join()
        self.one_publisher_completed()

    def is_buffer_full(self):
        return self._com_channel.full()

    def is_buffer_empty(self):
        return self._com_channel.empty()

    def __len__(self):
        self._com_channel.qsize()
