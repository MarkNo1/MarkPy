from dataclasses import dataclass
from ..thread import Thread


@dataclass(unsafe_hash=True, init=False)
class ThreadConsumer(Thread):
    _class_name = 'ThreadConsumer'

    def run(self):
        self._thread_init()
        try:
            while not self._thread_completed:
                if not self._thread_com_channel.is_buffer_empty():
                    obj = self._thread_com_channel.receive(block=self._thread_com_block,
                                                           timeout=self._thread_com_block_timeout)
                    if obj is not None:
                        self._thread_task(obj)
                        self._thread_com_channel.send_ack_message_processed()
                else:
                    if self._thread_com_channel.is_communication_completed():
                        self.set_thread_completed()
            self._thread_cleanup()

        except Exception as Ex:
            self.log.error(f'Error in execution: {Ex}')
