import unittest

from markipy.classes.path import Path
from markipy.classes.file import TextFile, YmlFile
from markipy.classes.folder import Folder
from markipy.classes.logger import Logger
from markipy import _unittest_default_dir

ws = dict(_class_working_path=_unittest_default_dir)

LOGGER = Logger(_class_working_path=_unittest_default_dir,
                _log_path=_unittest_default_dir,
                _log_file_name='UTest-File.log',
                _log_mode=Logger.LoggerMode.file)

LOGGER.log.debug("Starting UTest")

TM = '''\
author: TM
nick: Markno1
doc: "This is a possible class factory. @TM<3"
'''
# Imagine = @do import numpy; np.array()


io_param = dict(
    _class_working_path=Path('/tmp/unittest/'),
    _file_name='io.yml',
    **LOGGER.share_logger()
)

file_name = "TextFile.txt"
file_name_dfl = 'TextFileDefault.txt'
file_name_yml = "YmlFile.yml"


def test_write(filename, text):
    f = Folder(_folder_path='/tmp/unittest', _folder_auto_make=True)
    ft = TextFile(**ws, _file_mode=TextFile.FileMode.write, _file_name=filename)
    ft.open()
    ft.write(text)
    ft.close()


class TestTextFile(unittest.TestCase):

    def test_file_text_read(self):
        test_write(file_name, 'TEST')
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=file_name)
        ft.open()
        var = ft.read()
        ft.close()
        self.assertEqual(var, "TEST")

    def test_default_open_file_text_read(self):
        test_write(file_name_dfl, 'TEST-2')
        ft = TextFile(**ws, _file_mode=TextFile.FileMode.read, _file_name=file_name_dfl, _file_default_open=True)
        var = ft.read()
        self.assertEqual(var, "TEST-2")


YAML_CFG_TEST = '''\
name: to-init
val_1: 1
val_2: 2.0
val_3: 1e0
val_4: 1e0 * 4
val_5: [5]
val_6: "@do hash('a6')"
val_7: "@do dict(hash=hash('b7'))"
'''


def compare_target_config(cfg):
    def compare(a, b):
        res = a == b
        if res:
            return True
        else:
            print(f"[error-comparison]: {a} == {b}")
        return

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


class TestYmlFile(unittest.TestCase):

    def test_yml_io(self):
        TextFile(**io_param).write(YAML_CFG_TEST)
        cfg = YmlFile(**io_param, _file_mode=YmlFile.FileMode.read).read()
        self.assertEqual(compare_target_config(cfg), True)
