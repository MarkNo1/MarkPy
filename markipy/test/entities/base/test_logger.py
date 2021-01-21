import logging
import unittest
from time import sleep
from logging.handlers import TimedRotatingFileHandler
from markipy.entities.base import Path, Logger

working_dir = Path().cwd()

test_0_params = dict(
    _meta_name='Logger',
    _meta_cwd_path=working_dir,
    _log_path=working_dir / 'log',
    _cfg_path=working_dir / 'cfg'
)


class TestLoggerClass(unittest.TestCase):

    def test_logger_init(self):
        l = Logger(**test_0_params)

    def test_console_logger(self):
        ls = Logger(**test_0_params, _log_mode_=Logger.LoggerMode.console)
        self.assertEqual(ls._log_path, test_0_params['_log_path'])
        self.assertEqual(ls._log_mode_, Logger.LoggerMode.console)
        self.assertEqual(isinstance(ls.log, logging.LoggerAdapter), True)
        self.assertEqual(isinstance(ls._log_console_handler_, logging.StreamHandler), True)
        ls.log.debug('test_console_logger')
        sleep(0.05)
        del ls

    def test_file_logger(self):
        ls = Logger(**test_0_params, _log_mode_=Logger.LoggerMode.file)
        self.assertEqual(ls._log_path, test_0_params['_log_path'])
        self.assertEqual(ls.get_log_path(), test_0_params['_log_path'] / 'Logger.log')
        self.assertEqual(ls._log_mode_, Logger.LoggerMode.file)
        self.assertEqual(isinstance(ls.log, logging.LoggerAdapter), True)
        self.assertEqual(isinstance(ls._log_file_handler_, TimedRotatingFileHandler), True)
        ls.log.debug("test_file_logger")
        sleep(0.05)
        del ls
