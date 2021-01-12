from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.file import TextFile
from markipy.classes.communication.channels.int import MessageQueue

from markipy.classes.thread import Thread
from markipy.classes.thread.worker import ThreadProducer, ThreadConsumer

ws = dict(_class_working_path=Path('/tmp/unittest/'))

thread_general_txt_to_write = 'THREAD-TEST'


class TestThread(unittest.TestCase):
    class ThreadExample(Thread):
        def __init__(self, filename, **kwargs):
            Thread.__init__(self, **kwargs)
            self.filename = filename
            self.file = None

        def _thread_init(self):
            self.file = TextFile(**ws, _file_name=self.filename, _file_mode=TextFile.FileMode.write)
            self.file.open()

        def _thread_task(self):
            self.file.write(thread_general_txt_to_write)

        def _thread_cleanup(self):
            self.file.close()

    def test_general_thread(self):
        file_name = 'thread_general_test.txt'
        t = self.ThreadExample(file_name)
        t.start()
        t.join()
        self.assertEqual(True, Path(f'/tmp/unittest/{file_name}').exists())
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=file_name, _file_default_open=True)
        self.assertEqual(thread_general_txt_to_write, ft.read())


class TestWorkersThreads(unittest.TestCase):
    class ThreadProducerExample(ThreadProducer):

        def _thread_init(self):
            pass

        def _thread_task(self, *args, **kwargs):
            for i in range(0, 100):
                self.produce(i)
            self.producer_complete()

        def _thread_cleanup(self):
            pass

    class ThreadConsumerExample(ThreadConsumer):
        obj_received = None

        def _thread_init(self):
            self.obj_received = []

        def _thread_task(self, obj):
            self.obj_received.append(obj)

        def _thread_cleanup(self):
            pass

    def test_worker_producer_consumer(self):
        channel_mq = MessageQueue()
        tp = self.ThreadProducerExample(_thread_com_channel=channel_mq)
        tc = self.ThreadConsumerExample(_thread_com_channel=channel_mq)
        tp.start()
        tc.start()
        tp.join()
        tc.join()
        objs = [x for x in range(0, 100)]
        self.assertEqual(objs, tc.obj_received)


if __name__ == '__main__':
    unittest.main()
