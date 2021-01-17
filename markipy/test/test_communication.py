import unittest

from markipy.classes.path import Path
from markipy.classes.communication.channels.int import MessageQueue

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestCommunication(unittest.TestCase):

    def test_message_queue(self):
        mq = MessageQueue()
        mq.send(1)
        a = mq.receive()
        mq.send_ack_message_processed()
        mq.wait_completion_buffer()
        self.assertEqual(1, a)


if __name__ == '__main__':
    unittest.main()
