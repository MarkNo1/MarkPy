from dataclasses import dataclass

from ..base import BaseClass, update_kwargs_param_if_needed
from .logger_style import LoggerStyleMeta
from .logger_meta import LoggerMeta

from logging import StreamHandler, LoggerAdapter

import logging
from logging.handlers import TimedRotatingFileHandler


@dataclass(init=False, unsafe_hash=True)
class Logger(BaseClass, LoggerMeta, LoggerStyleMeta):
    def __init__(self, **kwargs):
        kwargs = update_kwargs_param_if_needed(kwargs, {'_class_name': 'Logger'})
        BaseClass.__init__(self, **kwargs)
        LoggerMeta.__init__(self, **kwargs)
        LoggerStyleMeta.__init__(self, **kwargs)

        self._log_file_path = self._log_path / self._log_file_name

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
        if self._log_mode == self.LoggerMode.from_other_logger:
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))