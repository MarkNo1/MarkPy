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

_console_logger_ = {'class': 'ConsoleLogger', 'version': 5,
                    }

_file_logger_ = {'class': 'FileLogger', 'version': 5,
                 'formatter': Formatter('[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d\n'
                                        '|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s')}




class Logger(Style):

    def __init__(self, console=True, file_log=None,  rotation='d', level=logging.DEBUG):
        Style.__init__(self)
        Atom.__init__(self, _logger_['class'], _logger_['version'])

        if not self._history(_logger_['class']).was_init:
            # Logger
            self.__logger__ = logging.getLogger(str(self._get_classes_hash()))
            # Set Level
            self.__logger__.setLevel(level)
            # Enable Console Logger
            if console: 
                self.__console_handler__ = logging.StreamHandler()
                self.__console_handler__.setFormatter(_logger_['console_formatter'])
                self.__logger__.addHandler(self.__console_handler__)
            # Enable File Logger
            if file_log:
                file_log = Path(DEFAULT_LOG_PATH) / f'{ str(file_log).replace("/",".") }.{date.today()}.log'
                self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(file_log, when=rotation, backupCount=5)
                self.__file_handler__.setFormatter(_logger_['file_formatter'])
                self.__logger__.addHandler(self.__file_handler__)

            # Set class init too True
            self._history.set_class_init(_logger_['class'])
            self.log = logging.LoggerAdapter(self.__logger__, {"atom_name": self._get_classes_name_str(), "atom_version": self._get_classes_versions_str()})



  

    def error(self, text):
        return self.red(text)

    def success(self, text):
        return self.green(text)

    def warning(self, text):
        return self.orange(text)

    def highlight(self, text):
        return self.blue(text)


