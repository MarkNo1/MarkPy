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

_base_logger_ = {'class': 'BaseLogger', 'version': 4}

_console_logger_ = {'class': 'ConsoleLogger', 'version': 5,
                    'formatter': Formatter(
                        '[%(asctime)s]|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s')}

_file_logger_ = {'class': 'FileLogger', 'version': 5,
                 'formatter': Formatter('[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d\n'
                                        '|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s')}

_logger_ = {'class': 'Logger', 'version': 7}


class BaseLogger(Style):

    def __init__(self, level=logging.DEBUG):
        Style.__init__(self)
        Atom.__init__(self, _base_logger_['class'], _base_logger_['version'])

        # Logger
        self.__logger__ = logging.getLogger(str(self._get_class_hash()))
        # Set Level
        self.__logger__.setLevel(level)

        # Prepare Logger Adapter
        self.log = None

    def _update_log_adapter(self):
        self.log = logging.LoggerAdapter(self.__logger__, {"atom_name": self._get_atom_inherit_classes_logs(),
                                                           "atom_version": self._get_atom_inherit_versions_logs()})

    def error(self, text):
        return self.red(text)

    def success(self, text):
        return self.green(text)

    def warning(self, text):
        return self.orange(text)

    def highlight(self, text):
        return self.blue(text)


class ConsoleLogger(BaseLogger):

    def __init__(self, level=logging.DEBUG):
        BaseLogger.__init__(self, level=level)
        Atom.__init__(self, _console_logger_['class'], _console_logger_['version'])

        self.__console_handler__ = logging.StreamHandler()
        self.__console_handler__.setFormatter(_console_logger_['formatter'])
        self.__logger__.addHandler(self.__console_handler__)
        self._update_log_adapter()


class FileLogger(BaseLogger):
    def __init__(self, log_file, level=logging.DEBUG, rotation='d'):
        BaseLogger.__init__(self, level)
        Atom.__init__(self, _file_logger_['class'], _file_logger_['version'])

        self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(log_file, when=rotation, backupCount=5)
        self.__file_handler__.setFormatter(_file_logger_['formatter'])
        self.__logger__.addHandler(self.__file_handler__)
        self._update_log_adapter()


class Logger(ConsoleLogger, FileLogger):
    def __init__(self, logFile, logPath=DEFAULT_LOG_PATH, level=logging.DEBUG):
        # if _console_logger_['class'] not in self._get_atom_inherit_classes():
        ConsoleLogger.__init__(self, level)
        # if _file_logger_['class'] not in self._get_atom_inherit_classes():
        FileLogger.__init__(self, Path(logPath) / f'{logFile}.{date.today()}.log', level)
        Atom.__init__(self, _logger_['class'], _logger_['version'])
        self._update_log_adapter()
