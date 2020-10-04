import time
from dataclasses import dataclass
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
from datetime import date

from .atom import Atom
from .perf import Performance
from .style import Style

DEFAULT_LOG_PATH = Path('/var/MarkPy/')

_logger_ = {'class': 'Logger', 'version': 7,
'console_formatter': Formatter('[%(asctime)s]|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s'),
'file_formatter': Formatter('[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d\n|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s')}


class Logger(Style):

    def __init__(self, console=True, file_log=None,  rotation='d', level=logging.DEBUG):
        Style.__init__(self)
        Atom.__init__(self, _logger_['class'], _logger_['version'])
        self._logger_console = console
        self._logger_file = file_log
        self._logger_rotatation = rotation
        self._logger_level = level
        self._init_atom_register_class(_logger_)


    def _init_atom_register_class(self, class_details):
        Atom.__init__(self, class_details['class'], class_details['version'])
        # Logger
        self.__logger__ = logging.getLogger(str(self._get_classes_hash()))
        # Set Level
        self.__logger__.setLevel(self._logger_level)
        # Enable Console Logger
        if self._logger_console: 
            self.__console_handler__ = logging.StreamHandler()
            self.__console_handler__.setFormatter(_logger_['console_formatter'])
            self.__logger__.addHandler(self.__console_handler__)
        # Enable File Logger
        if self._logger_file:
            file_log = Path(DEFAULT_LOG_PATH) / f'{ str(self._logger_file).replace("/",".") }.{date.today()}.log'
            self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(file_log, when=self._logger_rotatation, backupCount=5)
            self.__file_handler__.setFormatter(_logger_['file_formatter'])
            self.__logger__.addHandler(self.__file_handler__)

        self.log = logging.LoggerAdapter(self.__logger__, {"atom_name": self._get_classes_name_str(), "atom_version": self._get_classes_versions_str()})

    def error(self, text):
        return self.red(text)

    def success(self, text):
        return self.green(text)

    def warning(self, text):
        return self.orange(text)

    def highlight(self, text):
        return self.blue(text)


