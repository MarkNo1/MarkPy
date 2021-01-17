import logging
import unittest

from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
from pathlib import Path

from markipy.classes.logger import LoggerStyleMeta, LoggerMeta, Logger
from markipy import _log_default_dir


class TestLoggerClass(unittest.TestCase):

    def test_logger_style(self):
        ls = LoggerStyleMeta()

    def test_logger(self):
        ls = Logger()
        self.assertEqual(ls._log_path, _log_default_dir)
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.console)

    def test_logger_inheritance(self):
        class Test(Logger):
            pass

        ls = Test()
        self.assertEqual(ls._log_path, _log_default_dir)
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.console)

    def test_logger_inheritance_with_arguments(self):
        class TestArgs(Logger):
            pass

        ls = TestArgs(_class_name='TestArgs', _class_version='0.0.3')
        self.assertEqual(ls._log_path, _log_default_dir)
        self.assertEqual(ls._class_name, 'TestArgs')
        self.assertEqual(ls._class_version, '0.0.3')
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.console)

    def test_logger_inheritance_with_wrong_arguments(self):
        class TestArgsWrong(Logger):
            pass

        ls = TestArgsWrong(_class_name='TestArgsWrong', _class_version='0.0.3', ALBERO=28)
        self.assertEqual(ls._log_path, _log_default_dir)
        self.assertEqual(ls._class_name, 'TestArgsWrong')
        self.assertEqual(ls._class_version, '0.0.3')
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.console)

    def test_console_logger(self):
        ls = Logger(_log_mode=Logger.LoggerMode.console)
        self.assertEqual(ls._log_path, _log_default_dir)
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.console)
        self.assertEqual(isinstance(ls.log, logging.LoggerAdapter), True)
        self.assertEqual(isinstance(ls._log_console_handler, logging.StreamHandler), True)

    def test_file_logger(self):
        ls = Logger(_log_mode=Logger.LoggerMode.file)
        self.assertEqual(ls._log_path, _log_default_dir)
        self.assertEqual(ls._log_file_name, 'LoggerMeta.log')
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.file)
        self.assertEqual(isinstance(ls.log, logging.LoggerAdapter), True)
        self.assertEqual(isinstance(ls._log_file_handler, TimedRotatingFileHandler), True)

    def test_file_logger_custom_file(self):
        ls = Logger(_log_mode=Logger.LoggerMode.file, _log_path=Path('/tmp'), _log_file_name='TestFileLogger.log')
        self.assertEqual(ls._log_path, Path('/tmp'))
        self.assertEqual(ls._log_file_name, 'TestFileLogger.log')
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.file)
        self.assertEqual(isinstance(ls.log, logging.LoggerAdapter), True)
        self.assertEqual(isinstance(ls._log_file_handler, TimedRotatingFileHandler), True)
        ls.log.debug("TEST")

    def test_console_and_file_logger(self):
        ls = Logger(_log_mode=Logger.LoggerMode.console_and_file, _log_path=Path('/tmp'),
                    _log_file_name='TestConsoleFileLogger.log')
        self.assertEqual(ls._log_path, Path('/tmp'))
        self.assertEqual(ls._log_file_name, 'TestConsoleFileLogger.log')
        self.assertEqual(ls._log_mode, LoggerMeta.LoggerMode.console_and_file)
        self.assertEqual(isinstance(ls.log, logging.LoggerAdapter), True)
        self.assertEqual(isinstance(ls._log_console_handler, StreamHandler), True)
        self.assertEqual(isinstance(ls._log_file_handler, TimedRotatingFileHandler), True)
        ls.log.debug("TEST-1")


    def test_file_shared_logger(self):
        ol = Logger(_log_mode=Logger.LoggerMode.file, _log_path=Path('/tmp/unittest'),
                    _log_file_name='TestOtherLogger.log')

        lc = Logger(**ol.share_logger(), _class_name='SharedLogger')

        self.assertEqual(ol._log_path, lc._log_path)
        self.assertEqual(ol._log_file_name, lc._log_file_name)
        self.assertEqual(ol._log_logger, lc._log_logger)
        self.assertEqual(ol._log_console_handler, lc._log_console_handler)
        ol.log.debug("TEST-Original-Logger-1")
        lc.log.debug("TEST-Shared-Logger-1")
        ol.log.debug("TEST-Original-Logger-2")
        lc.log.debug("TEST-Shared-Logger-2")
        lc.log.debug("TEST-Shared-Logger-3")
        ol.log.debug("TEST-Original-Logger-3")
