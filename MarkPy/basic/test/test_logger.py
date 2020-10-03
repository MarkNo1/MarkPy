import unittest

from MarkPy.basic.style import _style_
from MarkPy.basic.atom import _atom_
from MarkPy.basic.logger import _base_logger_, _console_logger_

from MarkPy.basic import Atom
from MarkPy.basic import Style
from MarkPy.basic import BaseLogger, ConsoleLogger

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
        del a

    def test_console_logger_inheritance(self):
        c = ConsoleLoggerChild()
        self.assertEqual(c._get_atom_inherit_class(_atom_['class']).version, _atom_['version'])
        self.assertEqual(c._get_atom_inherit_class(_style_['class']).version, _style_['version'])
        self.assertEqual(c._get_atom_inherit_class(_base_logger_['class']).version, _base_logger_['version'])
        self.assertEqual(c._get_atom_inherit_class(_console_logger_['class']).version, _console_logger_['version'])

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


if __name__ == '__main__':
    unittest.main()
