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

_base_logger_ = {'class': 'BaseLogger', 'version': 4,
                 'formatter': Formatter('[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d\n'
                                        '|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s')}

_console_logger_ = {'class': 'ConsoleLogger', 'version': 5}

_file_logger_ = {'class': 'FileLogger', 'version': 5}

_logger_ = {'class': 'Logger', 'version': 7}


class BaseLogger(Style):

    def __init__(self, level=logging.DEBUG):
        Style.__init__(self)
        Atom.__init__(self, _base_logger_['class'], _base_logger_['version'])

        if _console_logger_['class'] not in self._get_atom_inherit_classes():
            # Logger
            self.__logger__ = logging.getLogger(str(self._get_class_hash()))
            # Set Level
            self.__logger__.setLevel(level)

        # Prepare Logger Adapter
        self.log = None

    def _set_format(self):
        return self._formatter

    # def __call__(self):
    #     return self.log

    # def __del__(self):
    #     self.log.debug(self.ugrey(f'Destructed'))

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

        # Logger
        if _console_logger_['class'] not in self._get_atom_inherit_classes():
            self.__console_handler__ = logging.StreamHandler()
            self.__console_handler__.setFormatter(self._set_format())
            self.__logger__.addHandler(self.__console_handler__)
            self._update_log_adapter()

# class FileLogger(BaseLogger):
#     version = _file_logger_['version']
#     name = _file_logger_['name']
#
#     @log_base_init
#     def __init__(self, log_file, loggerName='FileLogger', level=logging.DEBUG, rotation='d'):
#         BaseLogger.__init__(self, loggerName, level)
#
#         # Logger
#         self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(log_file, when=rotation, backupCount=5)
#         self.__file_handler__.setFormatter(self._set_format())
#         self.__logger__.addHandler(self.__file_handler__)
#
#     def __del__(self):
#         BaseLogger.__del__(self)
#
#
# class Logger(ConsoleLogger, FileLogger):
#     version = _logger_['version']
#     name = _logger_['name']
#
#     def __init__(self, loggerName='Logger', logPath=DEFAULT_LOG_PATH, level=logging.DEBUG):
#         if 'ConsoleLogger' not in self.getNames():
#             ConsoleLogger.__init__(self, loggerName, level)
#         if 'FileLogger' not in self.getNames():
#             FileLogger.__init__(self, Path(logPath) / f'{loggerName}.{date.today()}.log', loggerName, level)
#
#     def __del__(self):
#         FileLogger.__del__(self)


# def test_logger():
#     console_logger = ConsoleLogger()
#     file_logger = FileLogger('FileLogger.test')
#     logger = Logger('Logger.test')
#
#     # Console Logger
#     console_logger().info("** Testing ConsoleLogger Class **")
#     console_logger().info("START")
#     console_logger().debug('This is an example of a level of console_logger case of the type: debug')
#     console_logger().info('This is an example of a level of console_logger case of the type: info')
#     console_logger().warn('This is an example of a level of console_logger case of the type: warn')
#     console_logger().error('This is an example of a level of console_logger case of the type: error')
#     console_logger().error(
#         console_logger.error('This is an example of a level of console_logger case of the type: error with style'))
#     console_logger().info(
#         console_logger.highlight('This is an example of a level of console_logger case of the type: info with style'))
#     console_logger().warn(
#         console_logger.warning('This is an example of a level of console_logger case of the type: warn with style'))
#
#     # File logger
#     file_logger().info("** Testing FileLogger Class **")
#     file_logger().info("START")
#     file_logger().debug('This is an example of a level of file_logger case of the type: debug')
#     file_logger().info('This is an example of a level of file_logger case of the type: info')
#     file_logger().warn('This is an example of a level of file_logger case of the type: warn')
#     file_logger().error('This is an example of a level of file_logger case of the type: error')
#     file_logger().error(
#         file_logger.error('This is an example of a level of file_logger case of the type: error with style'))
#     file_logger().info(
#         file_logger.highlight('This is an example of a level of file_logger case of the type: info with style'))
#     file_logger().warn(
#         file_logger.warning('This is an example of a level of file_logger case of the type: warn with style'))
#
#     # Logger
#     logger().info("** Testing Logger Class **")
#     logger().info("START")
#     logger().debug('This is an example of a level of logger case of the type: debug')
#     logger().info('This is an example of a level of logger case of the type: info')
#     logger().warn('This is an example of a level of logger case of the type: warn')
#     logger().error('This is an example of a level of logger case of the type: error')
#     logger().error(logger.error('This is an example of a level of logger case of the type: error with style'))
#     logger().info(logger.highlight('This is an example of a level of logger case of the type: info with style'))
#     logger().warn(logger.warning('This is an example of a level of logger case of the type: warn with style'))
