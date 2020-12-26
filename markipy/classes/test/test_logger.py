import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from markipy.classes.test import unittest
from markipy.classes.logger import LoggerStyleMeta, LoggerMeta, Logger
from markipy import DEFAULT_LOG_PATH


class TestLoggerClass(unittest.TestCase):

    def test_logger_style(self):
        ls = LoggerStyleMeta()

    def test_logger(self):
        ls = Logger()
        self.assertEqual(ls._log_path, DEFAULT_LOG_PATH)
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.console)

    def test_logger_inheritance(self):
        class Test(Logger):
            pass

        ls = Test()
        self.assertEqual(ls._log_path, DEFAULT_LOG_PATH)
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.console)

    def test_logger_inheritance_with_arguments(self):
        class TestArgs(Logger):
            pass

        ls = TestArgs(_class_name='TestLogsArgs', _class_version='0.0.3')
        self.assertEqual(ls._log_path, DEFAULT_LOG_PATH)
        self.assertEqual(ls._class_name, 'TestLogsArgs')
        self.assertEqual(ls._class_version, '0.0.3')
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.console)

    def test_logger_inheritance_with_wrong_arguments(self):
        class TestArgsWrong(Logger):
            pass

        ls = TestArgsWrong(_class_name='TestLogsArgs', _class_version='0.0.3', ALBERO=28)
        self.assertEqual(ls._log_path, DEFAULT_LOG_PATH)
        self.assertEqual(ls._class_name, 'TestLogsArgs')
        self.assertEqual(ls._class_version, '0.0.3')
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.console)

    def test_console_logger(self):
        ls = Logger(_log_mode=Logger.Mode.console)
        self.assertEqual(ls._log_path, DEFAULT_LOG_PATH)
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.console)
        isinstance(ls.log, logging.LoggerAdapter)
        isinstance(ls._log_console_handler, logging.StreamHandler)

    def test_file_logger(self):
        ls = Logger(_log_mode=Logger.Mode.file)
        self.assertEqual(ls._log_path, DEFAULT_LOG_PATH)
        self.assertEqual(ls._log_file_name, 'LoggerMeta.log')
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.file)
        isinstance(ls.log, logging.LoggerAdapter)
        isinstance(ls._log_file_handler, TimedRotatingFileHandler)

    def test_file_logger_custom_file(self):
        ls = Logger(_log_mode=Logger.Mode.file, _log_path=Path('/tmp'), _log_file_name='TestFileLogger.log')
        self.assertEqual(ls._log_path, Path('/tmp'))
        self.assertEqual(ls._log_file_name, 'TestFileLogger.log')
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.file)
        isinstance(ls.log, logging.LoggerAdapter)
        isinstance(ls._log_file_handler, TimedRotatingFileHandler)
        ls.log.debug("TEST")

    def test_console_and_file_logger(self):
        ls = Logger(_log_mode=Logger.Mode.console_and_file, _log_path=Path('/tmp'),
                    _log_file_name='TestConsoleFileLogger.log')
        self.assertEqual(ls._log_path, Path('/tmp'))
        self.assertEqual(ls._log_file_name, 'TestConsoleFileLogger.log')
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.console_and_file)
        isinstance(ls.log, logging.LoggerAdapter)
        isinstance(ls._log_console_handler, TimedRotatingFileHandler)
        ls.log.debug("TEST")

    def test_file_from_other_logger(self):
        ol = Logger(_log_mode=Logger.Mode.console_and_file, _log_path=Path('/tmp/unittest'),
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
