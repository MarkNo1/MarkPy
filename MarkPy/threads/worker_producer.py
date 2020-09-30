from .worker_interface import IWorker


class WorkerProducer(IWorker):

    name = '[WorkerProducer]'

    def task(self):
        pass

    def run(self):
        self.init()
        try:
            while not self.finish:
                self.task()
        except Exception as e:
            self.logger(error=f"{self.name}: Error -> {e}")

    def set_finish(self):
        self.channel.wait_completion_task()
        self.finish = True
        self.cleanup()

    def produce(self, val):
        self.channel.put(val)
