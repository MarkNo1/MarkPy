from .worker_interface import IWorker


class WorkerConsumer(IWorker):

    name = '[WorkerConsumer]'

    def task(self, val):
        pass

    def run(self):
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
            self.logger(error=f"{self.name}: Error -> {e}")
