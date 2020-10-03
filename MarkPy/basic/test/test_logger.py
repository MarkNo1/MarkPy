import unittest

import HtmlTestRunner

from MarkPy.basic.style import _style_
from MarkPy.basic.atom import _atom_
from MarkPy.basic.logger import _base_logger_, _console_logger_, _file_logger_, _logger_

from MarkPy.basic import Atom
from MarkPy.basic import Style
from MarkPy.basic import BaseLogger, ConsoleLogger, FileLogger, Logger

_baselogger_child_ = {'class': 'BaseLoggerChild', 'version': 2}
_baselogger_nephew_ = {'class': 'BaseLoggerNephew', 'version': 3}


class BaseLoggerChild(BaseLogger):
    def __init__(self):
        BaseLogger.__init__(self)
        Atom.__init__(self, _baselogger_child_['class'], _baselogger_child_['version'])


class BaseLoggerNephew(BaseLoggerChild):
    def __init__(self):
        BaseLoggerChild.__init__(self)
        Atom.__init__(self, _baselogger_nephew_['class'], _baselogger_nephew_['version'])


class TestBaseLogger(unittest.TestCase):

    def test_base_logger_creation(self):
        a = BaseLogger()
        self.assertEqual(a._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        del a

    def test_base_logger_inheritance(self):
        c = BaseLoggerChild()
        self.assertEqual(c._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(c._get_atom_inherit_class(_baselogger_child_['class']).version, _baselogger_child_['version'])

    def test_base_logger_multiple_inheritance(self):
        n = BaseLoggerNephew()
        self.assertEqual(n._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_baselogger_child_['class']).version, _baselogger_child_['version'])
        self.assertEqual(n._get_atom_inherit_class(_baselogger_nephew_['class']).version,
                         _baselogger_nephew_['version'])


_consolelogger_child_ = {'class': 'ConsoleLoggerChild', 'version': 2}
_consolelogger_nephew_ = {'class': 'ConsoleLoggerNephew', 'version': 3}


class ConsoleLoggerChild(ConsoleLogger):
    def __init__(self):
        ConsoleLogger.__init__(self)
        Atom.__init__(self, _consolelogger_child_['class'], _consolelogger_child_['version'])


class ConsoleLoggerNephew(ConsoleLoggerChild):
    def __init__(self):
        ConsoleLoggerChild.__init__(self)
        Atom.__init__(self, _consolelogger_nephew_['class'], _consolelogger_nephew_['version'])


#
#
class TestConsoleLogger(unittest.TestCase):

    def test_console_logger_creation(self):
        a = ConsoleLogger()
        self.assertEqual(a._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(a._get_atom_inherit_class(_console_logger_['class']).version, _console_logger_['version'])
        a.log.debug("test_console_logger_creation")
        del a

    def test_console_logger_inheritance(self):
        c = ConsoleLoggerChild()
        self.assertEqual(c._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(c._get_atom_inherit_class(_console_logger_['class']).version, _console_logger_['version'])
        c.log.debug("test_console_logger_inheritance")

    def test_console_logger_multiple_inheritance(self):
        n = ConsoleLoggerNephew()
        self.assertEqual(n._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_console_logger_['class']).version, _console_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_consolelogger_child_['class']).version,
                         _consolelogger_child_['version'])
        self.assertEqual(n._get_atom_inherit_class(_consolelogger_nephew_['class']).version,
                         _consolelogger_nephew_['version'])
        n.log.debug("test_console_logger_multiple_inheritance")


_filelogger_child_ = {'class': 'FileLoggerChild', 'version': 2}
_filelogger_nephew_ = {'class': 'FileLoggerNephew', 'version': 3}


class FileLoggerChild(FileLogger):
    def __init__(self, file):
        FileLogger.__init__(self, file)
        Atom.__init__(self, _filelogger_child_['class'], _filelogger_child_['version'])


class FileLoggerNephew(FileLoggerChild):
    def __init__(self, file):
        FileLoggerChild.__init__(self, file)
        Atom.__init__(self, _filelogger_nephew_['class'], _filelogger_nephew_['version'])


#
#
class TestFileLogger(unittest.TestCase):

    def test_console_logger_creation(self):
        a = FileLogger('/tmp/test.FileLogger')
        self.assertEqual(a._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(a._get_atom_inherit_class(_file_logger_['class']).version, _file_logger_['version'])
        a.log.debug("test_file_logger_creation")
        del a

    def test_file_logger_inheritance(self):
        c = FileLoggerChild('/tmp/test.FileLogger')
        self.assertEqual(c._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(c._get_atom_inherit_class(_file_logger_['class']).version, _file_logger_['version'])
        c.log.debug("test_file_logger_inheritance")

    def test_file_logger_multiple_inheritance(self):
        n = FileLoggerNephew('/tmp/test.FileLogger')
        self.assertEqual(n._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_file_logger_['class']).version, _file_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_filelogger_child_['class']).version,
                         _filelogger_child_['version'])
        self.assertEqual(n._get_atom_inherit_class(_filelogger_nephew_['class']).version,
                         _filelogger_nephew_['version'])
        n.log.debug("test_file_logger_multiple_inheritance")


class LoggerChild(Logger):
    def __init__(self, file):
        Logger.__init__(self, file)
        Atom.__init__(self, _filelogger_child_['class'], _filelogger_child_['version'])


class LoggerNephew(LoggerChild):
    def __init__(self, file):
        LoggerChild.__init__(self, file)
        Atom.__init__(self, _filelogger_nephew_['class'], _filelogger_nephew_['version'])


#
#
class TestLogger(unittest.TestCase):

    def test_console_logger_creation(self):
        a = Logger('/tmp/test.Logger')
        self.assertEqual(a._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(a._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(a._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(a._get_atom_inherit_class(_file_logger_['class']).version, _file_logger_['version'])
        self.assertEqual(a._get_atom_inherit_class(_logger_['class']).version, _logger_['version'])
        a.log.debug("test_logger_creation")
        del a

    def test_file_logger_inheritance(self):
        c = LoggerChild('/tmp/test.Logger')
        self.assertEqual(c._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(c._get_atom_inherit_class(_file_logger_['class']).version, _file_logger_['version'])
        self.assertEqual(c._get_atom_inherit_class(_logger_['class']).version, _logger_['version'])
        c.log.debug("test_logger_inheritance")

    def test_file_logger_multiple_inheritance(self):
        n = LoggerNephew('/tmp/test.Logger')
        self.assertEqual(n._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(n._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(n._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_file_logger_['class']).version, _file_logger_['version'])
        self.assertEqual(n._get_atom_inherit_class(_filelogger_child_['class']).version,
                         _filelogger_child_['version'])
        self.assertEqual(n._get_atom_inherit_class(_filelogger_nephew_['class']).version,
                         _filelogger_nephew_['version'])
        self.assertEqual(n._get_atom_inherit_class(_logger_['class']).version, _logger_['version'])
        n.log.debug("test_logger_multiple_inheritance")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/tmp/markpy_unittest/'))
