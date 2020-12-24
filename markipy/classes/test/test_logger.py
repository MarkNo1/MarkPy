import logging
from logging.handlers import TimedRotatingFileHandler

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
        self.assertEqual(ls._log_file_path, DEFAULT_LOG_PATH / 'LoggerMeta.log')
        self.assertEqual(ls._log_mode, LoggerMeta.Mode.file)
        isinstance(ls.log, logging.LoggerAdapter)
        isinstance(ls._log_console_handler, TimedRotatingFileHandler)
