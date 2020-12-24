from dataclasses import dataclass

from ..base import BaseMeta
from .logger_style import LoggerStyleMeta
from .logger_meta import LoggerMeta

from logging import StreamHandler, FileHandler, LoggerAdapter

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import date


@dataclass
class Logger(BaseMeta, LoggerMeta, LoggerStyleMeta):
    def __init__(self, **kwargs):
        if '_class_name' not in kwargs:
            kwargs.update(dict(_class_name='Logger'))
        # Root Console Log
        BaseMeta.__init__(self, **kwargs)
        LoggerMeta.__init__(self, **kwargs)
        LoggerStyleMeta.__init__(self, **kwargs)

        if self._log_mode == self.Mode.console:
            self._log_logger = logging.getLogger()
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self.log = LoggerAdapter(self._log_logger,
                                     dict(class_name=self._class_name, class_version=self._class_version))

#
#
#
# class Logger(Style):
#
#     def _init_atom_register_class(self, class_details):
#         Atom.__init__(self, class_details['class'], class_details['version'])
#         # Logger
#         self.__logger__ = logging.getLogger(str(self._get_classes_hash()))
#         # Set Level
#         self.__logger__.setLevel(self._logger_level)
#         # Enable Console Logger
#         if self._logger_console:
#             self.__console_handler__ = logging.StreamHandler()
#             self.__console_handler__.setFormatter(_logger_['console_formatter'])
#             self.__logger__.addHandler(self.__console_handler__)
#         # Enable File Logger
#         if self._logger_file:
#             file_log = self.log_path / f'{str(self._logger_file).replace("/", ".")}.{date.today()}.log'
#             self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(file_log, when=self._logger_rotation,
#                                                                               backupCount=5)
#             self.__file_handler__.setFormatter(_logger_['file_formatter'])
#             self.__logger__.addHandler(self.__file_handler__)
#
#         self.log = logging.LoggerAdapter(self.__logger__, {"atom_name": class_details['class'],
#                                                            "atom_version": class_details['version']})
#
#         self.hlog = logging.LoggerAdapter(self.__logger__, {"atom_name": self._get_classes_name_str(),
#                                                            "atom_version": self._get_classes_versions_str()})
#
#         self.hlog.debug(" Init ")
#
#     def error(self, text):
#         return self.red(text)
#
#     def success(self, text):
#         return self.green(text)
#
#     def warning(self, text):
#         return self.orange(text)
#
#     def highlight(self, text):
#         return self.blue(text)
