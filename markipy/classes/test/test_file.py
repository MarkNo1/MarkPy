from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.file import TextFile

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestFile(unittest.TestCase):

    def test_file_text_initialization(self):
        file_name = "TextFile"
        ft = TextFile(**ws, _file_name=file_name)
        self.assertEqual(ft._file_name, file_name)
        self.assertEqual(ft._class_working_path, Path('/tmp/unittest/'))
        self.assertEqual(ft._file_path, Path('/tmp/unittest/') / file_name)

    def test_file_text_write(self):
        file_name = "TextFile"
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.write, _file_name=file_name)
        ft.open()
        ft.write("TEST")
        ft.close()

    def test_file_text_read(self):
        file_name = "TextFile"
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=file_name)
        ft.open()
        var = ft.read()
        ft.close()
        self.assertEqual(var, "TEST")


if __name__ == '__main__':
    unittest.main()
