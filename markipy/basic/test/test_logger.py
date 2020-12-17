from .common import unittest

from markipy.basic.style import _style_
from markipy.basic.atom import _atom_
from markipy.basic.logger import _logger_
from markipy.basic import Logger

from markipy import DEFAULT_UNITTEST_FOLDER, ensure_folder

WRK_DIR = DEFAULT_UNITTEST_FOLDER / 'logger'
LOG_DIR = WRK_DIR / 'logs'
ensure_folder(WRK_DIR)
ensure_folder(LOG_DIR)


_logger_child_ = {'class': 'LoggerChild', 'version': 2}
_logger_nephew_ = {'class': 'LoggerNephew', 'version': 3}


class LoggerChild(Logger):
    def __init__(self, console, file_log):
        Logger.__init__(self, console=console, file_log=file_log, log_path=LOG_DIR)
        self._init_atom_register_class(_logger_child_)


class LoggerNephew(LoggerChild):
    def __init__(self, console, file_log):
        LoggerChild.__init__(self, console=console, file_log=file_log )
        self._init_atom_register_class(_logger_nephew_)


class TestConsoleLogger(unittest.TestCase):

    def test_logger_creation(self):
        a = Logger(console=True)
        self.assertEqual(a._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_class_details(_logger_['class']).version, _logger_['version'])

    def test_logger_inheritance(self):
        c = LoggerChild(console=True, file_log=None)
        self.assertEqual(c._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(c._get_class_details(_logger_child_['class']).version, _logger_child_['version'])

    def test_logger_multiple_inheritance(self):
        n = LoggerNephew(console=True, file_log=None)
        self.assertEqual(n._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(n._get_class_details(_logger_child_['class']).version, _logger_child_['version'])
        self.assertEqual(n._get_class_details(_logger_nephew_['class']).version, _logger_nephew_['version'])


class TestFileLogger(unittest.TestCase):

    def test_logger_creation(self):
        a = Logger(console=False, file_log='test_file_logger', log_path=LOG_DIR)
        self.assertEqual(a._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_class_details(_logger_['class']).version, _logger_['version'])

    def test_logger_inheritance(self):
        c = LoggerChild(console=False, file_log='test_file_logger_inherit')
        self.assertEqual(c._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(c._get_class_details(_logger_child_['class']).version, _logger_child_['version'])

    def test_logger_multiple_inheritance(self):
        n = LoggerNephew(console=False, file_log='test_file_logger_multy_inherit')
        self.assertEqual(n._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(n._get_class_details(_logger_child_['class']).version, _logger_child_['version'])
        self.assertEqual(n._get_class_details(_logger_nephew_['class']).version, _logger_nephew_['version'])

    def test_logger_multiple_instances(self):
        n = LoggerNephew(console=False, file_log='test_file_logger_multy_instance_1')
        n.log.debug("init child")
        z = LoggerNephew(console=False, file_log='test_file_logger_multy_instance_2')
        z.log.debug("init nephew")
        n.log.debug("end child")
        z.log.debug("end nephew")

