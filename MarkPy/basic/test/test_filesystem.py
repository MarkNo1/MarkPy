import unittest

import HtmlTestRunner

from MarkPy.basic import Atom
from MarkPy.basic import File, Folder


_File_child_ = {'class': 'FileChild', 'version': 2}
_File_nephew_ = {'class': 'FileNephew', 'version': 3}


class FileChild(File):
    def __init__(self, console=False, file_path='/tmp/file_child_test'):
        File.__init__(self, console=console, file_path=file_path)
        self._init_atom_register_class(_File_child_)


class FileNephew(FileChild):
    def __init__(self, console=False, file_path='/tmp/file_nephew_test'):
        FileChild.__init__(self, console=console, file_path=file_path)
        self._init_atom_register_class(_File_nephew_)

class TestFile(unittest.TestCase):

    def test_performance_child(self):
        fc = FileChild()
        
        

    def test_performance_nephew(self):
        fn = FileNephew()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/tmp/markpy_unittest/'))
