from markipy.classes.test import unittest

from markipy.classes.path import Path
from markipy.classes.file import TextFile, YamlFile

ws = dict(_class_working_path=Path('/tmp/unittest/'))


class TestTextFile(unittest.TestCase):
    file_name = "TextFile.txt"
    file_name_dfl = 'TextFileDefault.txt'

    def test_file_text_initialization(self):
        ft = TextFile(**ws, _file_name=self.file_name, _file_mode=YamlFile.FileMode.write)
        self.assertEqual(ft._class_name, 'TextFile')
        self.assertEqual(ft._file_name, self.file_name)
        self.assertEqual(ft._class_working_path, Path('/tmp/unittest/'))
        self.assertEqual(ft._file_path, Path('/tmp/unittest/') / self.file_name)

    def test_file_text_write(self):
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.write, _file_name=self.file_name)
        ft.open()
        ft.write("TEST")
        ft.close()

    def test_file_text_read(self):
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=self.file_name)
        ft.open()
        var = ft.read()
        ft.close()
        self.assertEqual(var, "TEST")

    def test_default_open_file_text_write(self):
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.write, _file_name=self.file_name_dfl, _file_default_open=True)
        ft.write("TEST-2")

    def test_default_open_file_text_read(self):
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=self.file_name_dfl, _file_default_open=True)
        var = ft.read()
        self.assertEqual(var, "TEST-2")


YAML_CFG_TEST = '''
name: to-init
val_1: 1
val_2: 2.0
val_3: 1e0
val_4: 1e0 * 4
val_5: [5]
val_6: "@do hash('a6')"
val_7: "@do dict(hash=hash('b7'))"
'''


def compare(a, b):
    res = a == b
    if res:
        return True
    else:
        print(f"[error-comparison]: {a} == {b}")
    return


def compare_target_config(cfg):
    if compare(cfg['name'], 'to-init') and \
            compare(cfg['val_1'], 1) and \
            compare(cfg['val_2'], 2.0) and \
            compare(cfg['val_3'], 1e0) and \
            compare(cfg['val_4'], 1e0 * 4) and \
            compare(cfg['val_5'], [5]) and \
            compare(cfg['val_6'], hash('a6')) and \
            compare(cfg['val_7']['hash'], hash('b7')):
        return True
    else:
        return False


class TestYamlFile(unittest.TestCase):
    file_name = "YamlFile.yml"

    def test_file_yaml_initialization(self):
        ft = YamlFile(**ws, _file_name=self.file_name, _file_mode=YamlFile.FileMode.write)
        self.assertEqual(ft._class_name, 'YamlFile')
        self.assertEqual(ft._file_name, self.file_name)
        self.assertEqual(ft._class_working_path, Path('/tmp/unittest/'))
        self.assertEqual(ft._file_path, Path('/tmp/unittest/') / self.file_name)

    def test_file_yaml_write(self):
        ft = YamlFile(**ws, _file_mode=YamlFile.FileMode.write, _file_name=self.file_name)
        ft.open()
        ft.write(YAML_CFG_TEST)
        ft.close()

    def test_file_yaml_read(self):
        ft = YamlFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=self.file_name)
        ft.open()
        cfg = ft.read()
        ft.close()
        self.assertEqual(compare_target_config(cfg), True)


if __name__ == '__main__':
    unittest.main()
