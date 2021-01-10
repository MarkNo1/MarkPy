from dataclasses import dataclass
from ..thread import Thread


@dataclass(unsafe_hash=True, init=False)
class ThreadProducer(Thread):

    def run(self):
        self._thread_init()
        try:
            while not self._thread_completed:
                self._thread_task()
        except Exception as Ex:
            self.log.error(f'Error in execution: {Ex}')

    def produce(self, obj):
        self._thread_com_channel.send(obj, block=self._thread_com_block, timeout=self._thread_com_block_timeout)

    def producer_complete(self):
        if self._thread_com_channel is not None:
            self._thread_com_channel.wait_completion_buffer()
        self._thread_completed = True
        self._thread_cleanup()
