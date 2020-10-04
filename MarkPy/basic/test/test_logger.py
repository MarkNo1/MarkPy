import unittest

import HtmlTestRunner

from MarkPy.basic.style import _style_
from MarkPy.basic.atom import _atom_
from MarkPy.basic.logger import _logger_, _console_logger_, _file_logger_, _logger_

from MarkPy.basic import Atom
from MarkPy.basic import Style
from MarkPy.basic import Logger

_logger_child_ = {'class': 'LoggerChild', 'version': 2}
_logger_nephew_ = {'class': 'LoggerNephew', 'version': 3}


class LoggerChild(Logger):
    def __init__(self, console, file_log):
        Logger.__init__(self, console=console, file_log=file_log)
        Atom.__init__(self, _logger_child_['class'], _logger_child_['version'])


class LoggerNephew(LoggerChild):
    def __init__(self, console, file_log):
        LoggerChild.__init__(self, console=console, file_log=file_log)
        Atom.__init__(self, _logger_nephew_['class'], _logger_nephew_['version'])


class TestConsoleLogger(unittest.TestCase):

    def test_logger_creation(self):
        a = Logger(console=True)
        self.assertEqual(a._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_class_details(_logger_['class']).version, _logger_['version'])
        a.log.debug('test_logger_console_creation')

    def test_logger_inheritance(self):
        c = LoggerChild(console=True, file_log=None)
        self.assertEqual(c._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(c._get_class_details(_logger_child_['class']).version, _logger_child_['version'])
        c.log.debug('test_logger_console_inheritance')

    def test_logger_multiple_inheritance(self):
        n = LoggerNephew(console=True, file_log=None)
        self.assertEqual(n._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(n._get_class_details(_logger_child_['class']).version, _logger_child_['version'])
        self.assertEqual(n._get_class_details(_logger_nephew_['class']).version,_logger_nephew_['version'])
        n.log.debug('test_logger_console_multiple_inheritance')
    

class TestFileLogger(unittest.TestCase):

    def test_logger_creation(self):
        a = Logger(console=False, file_log='test_file_logger')
        self.assertEqual(a._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_class_details(_logger_['class']).version, _logger_['version'])
        a.log.debug('test_logger_file_creation')

    def test_logger_inheritance(self):
        c = LoggerChild(console=False, file_log='test_file_logger_inherit')
        self.assertEqual(c._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(c._get_class_details(_logger_child_['class']).version, _logger_child_['version'])
        c.log.debug('test_logger_file_inheritance')

    def test_logger_multiple_inheritance(self):
        n = LoggerNephew(console=False, file_log='test_file_logger_multy_inherit')
        self.assertEqual(n._get_class_details(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_class_details(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_class_details(_logger_['class']).version, _logger_['version'])
        self.assertEqual(n._get_class_details(_logger_child_['class']).version, _logger_child_['version'])
        self.assertEqual(n._get_class_details(_logger_nephew_['class']).version,_logger_nephew_['version'])
        n.log.debug('test_logger_file_multiple_inheritance')
    


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/tmp/markpy_unittest/'))
