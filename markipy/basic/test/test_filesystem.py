import unittest
import os
import HtmlTestRunner

from markipy.basic import Atom
from markipy.basic import File, Folder
from markipy import DEFAULT_UNITTEST_FOLDER, ensure_folder

WRK_DIR = DEFAULT_UNITTEST_FOLDER / 'filesytem'
LOG_DIR = WRK_DIR / 'logs'
ensure_folder(WRK_DIR)
ensure_folder(LOG_DIR)

_File_child_ = {'class': 'FileChild', 'version': 2}
_File_nephew_ = {'class': 'FileNephew', 'version': 3}


class FileChild(File):
    def __init__(self, console=False, file_path=WRK_DIR / 'file_child_unittest'):
        File.__init__(self, console=console, file_path=file_path, log_path=LOG_DIR)
        self._init_atom_register_class(_File_child_)


class FileNephew(FileChild):
    def __init__(self, console=False, file_path=WRK_DIR / 'file_nephew_unittest'):
        FileChild.__init__(self, console=console, file_path=file_path)
        self._init_atom_register_class(_File_nephew_)


class TestFile(unittest.TestCase):

    def test_file_child(self):
        fc = FileChild(file_path=WRK_DIR / 'file_child_unittest')
        self.assertEqual(os.path.exists(WRK_DIR / 'file_child_unittest'), True)

    def test_file_nephew(self):
        fn = FileNephew(file_path=WRK_DIR / 'file_nephew_unittest')
        self.assertEqual(os.path.exists(WRK_DIR / 'file_nephew_unittest'), True)


_Folder_child_ = {'class': 'FolderChild', 'version': 2}
_Folder_nephew_ = {'class': 'FolderNephew', 'version': 3}


class FolderChild(Folder):
    def __init__(self, console=False, folder_path=WRK_DIR / 'folder_child_unittest'):
        Folder.__init__(self, console=console, folder_path=folder_path, log_path=LOG_DIR)
        self._init_atom_register_class(_Folder_child_)


class FolderNephew(FolderChild):
    def __init__(self, console=False, folder_path=WRK_DIR / 'folder_nephew_unittest'):
        FolderChild.__init__(self, console=console, folder_path=folder_path)
        self._init_atom_register_class(_Folder_nephew_)


class TestFolder(unittest.TestCase):

    def test_performance_child(self):
        fc = FolderChild(folder_path=WRK_DIR / 'folder_child_unittest')
        self.assertEqual(os.path.exists(WRK_DIR / 'folder_child_unittest'), True)

    def test_performance_nephew(self):
        fn = FolderNephew(folder_path=WRK_DIR / 'folder_nephew_unittest')
        self.assertEqual(os.path.exists(WRK_DIR / 'folder_nephew_unittest'), True)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=WRK_DIR / 'markpy_unittest/'))
