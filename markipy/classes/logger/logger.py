from dataclasses import dataclass

from ..base import BaseMeta, update_kwargs_param_if_needed
from .logger_style import LoggerStyleMeta
from .logger_meta import LoggerMeta

from logging import StreamHandler, LoggerAdapter

import logging
from logging.handlers import TimedRotatingFileHandler


@dataclass(init=False, unsafe_hash=True)
class Logger(BaseMeta, LoggerMeta, LoggerStyleMeta):
    def __init__(self, **kwargs):
        kwargs = update_kwargs_param_if_needed(kwargs, {'_class_name': 'Logger'})
        BaseMeta.__init__(self, **kwargs)
        LoggerMeta.__init__(self, **kwargs)
        LoggerStyleMeta.__init__(self, **kwargs)

        # Console Logger
        if self._log_mode == self.Mode.console:
            self._log_logger = logging.getLogger()
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File Logger
        if self._log_mode == self.Mode.file:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_file_handler = TimedRotatingFileHandler(self._log_path / self._log_file_name,
                                                              when=self._log_rotation, interval=1, backupCount=2)
            self._log_file_handler.setFormatter(self._log_file_format)
            self._log_logger.addHandler(self._log_file_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))
            self._log_file_handler.doRollover()

        # File and Console Logger
        if self._log_mode == self.Mode.console_and_file:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self._log_file_handler = TimedRotatingFileHandler(self._log_path / self._log_file_name,
                                                              when=self._log_rotation, interval=1)
            self._log_file_handler.setFormatter(self._log_file_format)
            self._log_logger.addHandler(self._log_file_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))
            self._log_file_handler.doRollover()
