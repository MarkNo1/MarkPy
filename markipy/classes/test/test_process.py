from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.file import TextFile

from markipy.classes.process import Process

ws = dict(_class_working_path=Path('/tmp/unittest/'))
file_name = 'test-process-file.txt'
test_text = 'TEST-PROCESS'


class ExampleProcessTask(Process):
    _file: TextFile = None

    def _process_init(self):
        self._file = TextFile(**ws, _file_name=file_name, _file_mode=TextFile.FileMode.write)
        self._file.open()

    def _process_task(self, txt: object = None):
        self._file.write(test_text)

    def _process_cleanup(self):
        self._file.close()


class TestProcess(unittest.TestCase):
    def test_process_task(self):
        p = ExampleProcessTask()
        p.start()
        p.join()
        self.assertEqual(True, Path('/tmp/unittest/test-process-file.txt').exists())
        self.assertEqual(
            TextFile(**p.share_logger(), **ws, _file_name=file_name, _file_default_open=True,
                     _file_mode=TextFile.FileMode.read).read(),
            test_text)


if __name__ == '__main__':
    unittest.main()
