import threading


class IWorker(threading.Thread):
    def __init__(self, channel, logger):
        threading.Thread.__init__(self)
        self.channel = channel
        self.finish = False
        self.logger = logger
        self.name = '[IWorker]'
        self.setDaemon(True)

    def set_finish(self):
        self.finish = True
        self.cleanup()

    def init(self):
        pass

    def cleanup(self):
        pass


class GeneralWorker(IWorker):
    def __init__(self, logger):
        IWorker.__init__(self, None, logger)
        self.name = '[GeneralWorker]'

    def task(self):
        pass

    def run(self):
        self.init()
        self.task()
        self.cleanup()
