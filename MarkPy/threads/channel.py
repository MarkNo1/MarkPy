from queue import Queue


class Channel:
    def __init__(self, size=12500):
        self.queue = Queue(size)
        self.finish = False
        self.empty = Queue.empty

    def get(self):
        try:
            return self.queue.get(block=True, timeout=5)
        except Exception as e:
            return self.empty

    def put(self, var):
        self.queue.put(var, block=True)

    def task_done(self):
        self.queue.task_done()

    def set_finish(self):
        self.finish = True

    def get_finish(self):
        return self.finish

    def wait_completion_task(self):
        self.queue.join()
        self.set_finish()
