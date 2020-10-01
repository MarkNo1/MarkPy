import threading

from .channel import Channel
from .logger import Logger


class IThread(threading.Thread, Logger):

    __ithread_version__: str = '2'
    channel : Channel = None
    finish : bool = False

    def __init__(self, channel=None, name='IThread'):
        threading.Thread.__init__(self)
        Logger.__init__(self, f'.thread.{name}')
        self.newLogAtom('IThread', self.__ithread_version__)
        self.setDaemon(True)
        self.channel = channel
        self.log.debug(self.ugrey(f'Initialized'))

    def set_finish(self):
        self.finish = True
        self.cleanup()

    def init(self):
        pass

    def cleanup(self):
        pass


class GeneralThread(IThread):
    __general_thread_version__ : str = '2'

    def __init__(self, channel=None, name='GeneralThread'):
        IThread.__init__(self, channel, name)
        self.newLogAtom('GeneralThread', self.__general_thread_version__)
        self.log.debug(self.ugrey(f'Initialized'))

    def task(self):
        pass

    def run(self):
        self.log.debug('Starting thread')
        self.init()
        self.task()
        self.cleanup()
        self.log.debug('End thread')


class ThreadConsumer(IThread):

    __thread_consumer_version__ : str = '2'

    def __init__(self, channel=None, name='ThreadConsumer'):
        IThread.__init__(self, channel, name)
        self.newLogAtom('ThreadConsumer', self.__thread_consumer_version__)
        self.log.debug(self.ugrey(f'Initialized'))

    def task(self, val):
        pass

    def run(self):
        self.log.debug('Starting thread')
        self.init()
        try:
            while not self.finish:
                val = self.channel.get()
                if val is self.channel.empty:
                    if self.channel.get_finish():
                        self.set_finish()
                else:
                    if val is not None:
                        self.task(val)
                        self.channel.task_done()

        except Exception as e:
            self.log.error(f"Error -> {e}")
        self.log.debug('End thread')

class ThreadProducer(IThread):

    __thread_producer_version__ : str = '2'

    def __init__(self, channel=None, name='ThreadConsumer'):
        IThread.__init__(self, channel, name)
        self.newLogAtom('ThreadProducer', self.__thread_producer_version__)
        self.log.debug(self.ugrey(f'Initialized'))

    def task(self):
        pass

    def run(self):
        self.log.debug('Starting thread')
        self.init()
        try:
            while not self.finish:
                self.task()
        except Exception as e:
            self.log.error(f"Error -> {e}")
        self.log.debug('End thread')

    def set_finish(self):
        self.channel.wait_completion_task()
        self.finish = True
        self.cleanup()

    def produce(self, val):
        self.channel.put(val)
