from dataclasses import dataclass

from ..base import BaseClass
from ..path import Path
from .logger_style import LoggerStyleMeta
from .logger_meta import LoggerMeta

from logging import StreamHandler, LoggerAdapter

import logging
from logging.handlers import TimedRotatingFileHandler


def has_logger_class(cls):
    return hasattr(cls, 'log')


@dataclass(init=False, unsafe_hash=True)
class Logger(BaseClass, LoggerMeta, LoggerStyleMeta):

    def __init__(self, **kwargs):
        BaseClass.__init__(self, **kwargs)
        LoggerMeta.__init__(self, **kwargs)
        LoggerStyleMeta.__init__(self, **kwargs)

        self._log_file_path = Path(self._log_path) / Path(self._log_file_name)

        if self._log_if_exist_use_it:
            if has_logger_class(self) and self._log_logger is not None:
                self._log_mode = self.LoggerMode.shared_logger

        # Console Logger
        if self._log_mode == self.LoggerMode.console:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File Logger
        if self._log_mode == self.LoggerMode.file:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_file_handler = TimedRotatingFileHandler(self._log_file_path, when=self._log_rotation, interval=1,
                                                              backupCount=1)
            self._log_file_handler.doRollover()
            self._log_file_handler.setFormatter(self._log_file_format)
            self._log_logger.addHandler(self._log_file_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File and Console Logger
        if self._log_mode == self.LoggerMode.console_and_file:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self._log_file_handler = TimedRotatingFileHandler(self._log_file_path,
                                                              when=self._log_rotation, interval=1, backupCount=1)
            self._log_file_handler.doRollover()
            self._log_file_handler.setFormatter(self._log_file_format)
            self._log_logger.addHandler(self._log_file_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File logger from already exist Logger
        if self._log_mode == self.LoggerMode.shared_logger:
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))
