import time
from dataclasses import dataclass
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
from datetime import date

from .perf import Performance
from .style import Style

DEFAULT_LOG_PATH = Path('/var/MarkPy/')

_base_logger_ = {'name': lambda: 'BaseLogger', 'version': lambda: 4,
                 'formatter': lambda: Formatter('[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d\n'
                                                '|%(version)s|%(name)s %(levelname).4s:\t%(message)s')}

_console_logger_ = {'name': lambda: 'BaseLogger', 'version': lambda: 5}

_file_logger_ = {'name': lambda: 'FileLogger', 'version': lambda: 5}

_logger_ = {'name': lambda: 'Logger', 'version': lambda: 7}


def log_base_init(class_init):
    def init(base_class, name, version, *args, **kw):
        # Call class Constructor
        base_class = class_init(name, version, *args, **kw)
        # Register new class
        base_class.newAtom(base_class.sequential(base_class.name()), base_class.sequential(base_class.version()))
        logging.LoggerAdapter(base_class.__logger__, dict(name=base_class.name(), version=base_class.version()))
        base_class.log.debug(base_class.ugrey(f'Initialized'))
        return base_class

    return init


class BaseLogger(Style):
    version = _base_logger_['version']
    name = _base_logger_['name']
    _formatter = _base_logger_['formatter']

    log: logging.LoggerAdapter = None

    _hasBaseLogger = False
    performance = Performance()

    @log_base_init
    def __init__(self, loggerName, level=logging.DEBUG):
        if not self._hasBaseLogger:
            Style.__init__(self)
            # Logger
            self.__logger__ = logging.getLogger(loggerName)
            # Set Level
            self.__logger__.setLevel(level)
            # Do not re-init
            self._hasBaseLogger = True
        return self

    def _set_format(self):
        return self._formatter()

    def __call__(self):
        return self.log

    def __del__(self):
        self.log.debug(self.ugrey(f'Destructed'))

    def error(self, text):
        return self.red(text)

    def success(self, text):
        return self.green(text)

    def warning(self, text):
        return self.orange(text)

    def highlight(self, text):
        return self.blue(text)


class ConsoleLogger(BaseLogger):
    version = _console_logger_['version']
    name = _console_logger_['name']

    @log_base_init
    def __init__(self, loggerName='ConsoleLogger', level=logging.DEBUG):
        BaseLogger.__init__(self, loggerName, level)

        # Logger
        if not self.__logger__.hasHandlers():
            self.__console_handler__ = logging.StreamHandler()
            self.__console_handler__.setFormatter(self._set_format())
            self.__logger__.addHandler(self.__console_handler__)

        return self

    def __del__(self):
        BaseLogger.__del__(self)


class FileLogger(BaseLogger):
    version = _file_logger_['version']
    name = _file_logger_['name']

    @log_base_init
    def __init__(self, log_file, loggerName='FileLogger', level=logging.DEBUG, rotation='d'):
        BaseLogger.__init__(self, level)

        # Logger
        self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(log_file, when=rotation, backupCount=5)
        self.__file_handler__.setFormatter(self._set_format())
        self.__logger__.addHandler(self.__file_handler__)

        return self

    def __del__(self):
        BaseLogger.__del__(self)


class Logger(ConsoleLogger, FileLogger):
    version = _logger_['version']
    name = _logger_['name']

    def __init__(self, loggerName='Logger', logPath=DEFAULT_LOG_PATH, level=logging.DEBUG):
        if 'ConsoleLogger' not in self.getAtomName():
            ConsoleLogger.__init__(self, loggerName, level)
        if 'FileLogger' not in self.getAtomName():
            FileLogger.__init__(self, Path(logPath) / f'{loggerName}.{date.today()}.log', loggerName, level)

        return self

    def __del__(self):
        FileLogger.__del__(self)


def test_logger():
    console_logger = ConsoleLogger()
    file_logger = FileLogger('FileLogger.test')
    logger = Logger('Logger.test')

    # Console Logger
    console_logger().info("** Testing ConsoleLogger Class **")
    console_logger().info("START")
    console_logger().debug('This is an example of a level of console_logger case of the type: debug')
    console_logger().info('This is an example of a level of console_logger case of the type: info')
    console_logger().warn('This is an example of a level of console_logger case of the type: warn')
    console_logger().error('This is an example of a level of console_logger case of the type: error')
    console_logger().error(
        console_logger.error('This is an example of a level of console_logger case of the type: error with style'))
    console_logger().info(
        console_logger.highlight('This is an example of a level of console_logger case of the type: info with style'))
    console_logger().warn(
        console_logger.warning('This is an example of a level of console_logger case of the type: warn with style'))

    # File logger
    file_logger().info("** Testing FileLogger Class **")
    file_logger().info("START")
    file_logger().debug('This is an example of a level of file_logger case of the type: debug')
    file_logger().info('This is an example of a level of file_logger case of the type: info')
    file_logger().warn('This is an example of a level of file_logger case of the type: warn')
    file_logger().error('This is an example of a level of file_logger case of the type: error')
    file_logger().error(
        file_logger.error('This is an example of a level of file_logger case of the type: error with style'))
    file_logger().info(
        file_logger.highlight('This is an example of a level of file_logger case of the type: info with style'))
    file_logger().warn(
        file_logger.warning('This is an example of a level of file_logger case of the type: warn with style'))

    # Logger
    logger().info("** Testing Logger Class **")
    logger().info("START")
    logger().debug('This is an example of a level of logger case of the type: debug')
    logger().info('This is an example of a level of logger case of the type: info')
    logger().warn('This is an example of a level of logger case of the type: warn')
    logger().error('This is an example of a level of logger case of the type: error')
    logger().error(logger.error('This is an example of a level of logger case of the type: error with style'))
    logger().info(logger.highlight('This is an example of a level of logger case of the type: info with style'))
    logger().warn(logger.warning('This is an example of a level of logger case of the type: warn with style'))


if __name__ == '__main__':
    l = Logger()
    l.log.debug('It Works !')
