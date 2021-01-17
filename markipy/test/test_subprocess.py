import unittest

from markipy.classes.path import Path
from markipy.classes.communication.channels.int import MessageQueue

from markipy.classes.subprocess import SubProcess

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestSubProcess(unittest.TestCase):

    def test_subprocess_cmd_passing(self):
        cmd = 'mkdir -p test_process_folder'
        sp = SubProcess(_process_cmd=cmd)
        self.assertEqual(sp._process_cmd, cmd)

    def test_subprocess_task(self):
        cmd = 'mkdir -p test_process_folder'
        sp = SubProcess(_process_cmd=cmd, **ws)
        sp.start()
        sp.join()
        self.assertEqual(Path('/tmp/unittest/test_process_folder').exists(), True)

    def test_subprocess_task_retrieve_stdout(self):
        text = 'Process Output'
        cmd = f'echo "{text}"'
        mq = MessageQueue()
        sp = SubProcess(_process_cmd=cmd, _process_com_channel=mq, **ws)
        sp.start()
        sp.join()
        self.assertEqual(Path('/tmp/unittest/test_process_folder').exists(), True)
        proc_stdout = mq.receive()
        self.assertEqual(proc_stdout, text)


if __name__ == '__main__':
    unittest.main()
