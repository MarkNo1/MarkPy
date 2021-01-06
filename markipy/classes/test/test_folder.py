from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.folder import Folder

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestFolder(unittest.TestCase):

    def test_folder_one_path_not_exist(self):
        f_path = '/tmp/test_folder_not_created'
        f = Folder(_folder_path=f_path)
        self.assertNotEqual(True, Path(f_path).exists())

    def test_folder_one_path_create(self):
        f_path = '/tmp/test_folder_created'
        f = Folder(_folder_path=f_path)
        f.make()
        self.assertEqual(True, Path(f_path).exists())

    def test_folder_one_path_auto_create(self):
        f_path = '/tmp/test_folder_auto_make'
        f = Folder(_folder_path=f_path, _folder_auto_make=True)
        self.assertEqual(True, Path(f_path).exists())

    def test_folder_multi_path_auto_create(self):
        f_path = '/tmp/unittest/1/2/3/test_folder_auto_make'
        f = Folder(_folder_path=f_path, _folder_auto_make=True)
        self.assertEqual(True, Path(f_path).exists())


if __name__ == '__main__':
    unittest.main()
