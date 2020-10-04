import unittest

import HtmlTestRunner

from MarkPy.basic import Atom
from MarkPy.basic import File, Folder


_logger_child_ = {'class': 'LoggerChild', 'version': 2}
_logger_nephew_ = {'class': 'LoggerNephew', 'version': 3}


class LoggerChild(Logger):
    def __init__(self, console, file_log):
        Logger.__init__(self, console=console, file_log=file_log)
        self._init_atom_register_class(_logger_child_)


class LoggerNephew(LoggerChild):
    def __init__(self, console, file_log):
        LoggerChild.__init__(self, console=console, file_log=file_log)
        self._init_atom_register_class(_logger_nephew_)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/tmp/markpy_unittest/'))
