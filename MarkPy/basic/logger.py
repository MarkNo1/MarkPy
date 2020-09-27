from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

from MarkPy.atom import Atom


# Log Format
Format = '''{%(pathname)s:%(lineno)d}\t%(levelname).4s\t%(asctime)s\t%(process)d\t%(name)s\t%(message)s'''

# Every Day
FileRotation = 'd'

__version__ = '1.0.0'

class BaseLogger(Atom):
    def __init__(self, name, level=logging.DEBUG):
        Atom.__init__(self, name, self.__class__)
        # Logger
        self.__logger__ = logging.getLogger(name)
        # Set Level default DEBUG
        self.__logger__.setLevel(level)

    def __call__(self):
        return self.__logger__

    def log(self):
        return self.__logger__


class ConsoleLogger(BaseLogger):
    def __init__(self, name, level=logging.DEBUG):
        BaseLogger.__init__(self, name, level)
        # Logger
        self.__console_handler__ = logging.StreamHandler()
        self.__console_handler__.setFormatter(Formatter(Format))
        self.__logger__.addHandler(self.__console_handler__)


class FileLogger(BaseLogger):
    def __init__(self, name, log_file, level=logging.DEBUG):
        BaseLogger.__init__(self, name, level)
        # Logger
        self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(log_file, when= FileRotation, backupCount=5)
        self.__file_handler__.setFormatter(Formatter(Format))
        self.__logger__.addHandler(self.__file_handler__)


class Logger(ConsoleLogger, FileLogger):
    def __init__(self, name, file=None, level=logging.DEBUG):
        ConsoleLogger.__init__(self, name, level)
        FileLogger.__init__(self, name, Path(file) if file else Path.cwd() / Path(f'{name}.log'), level)


def test_logger():
    console_logger = ConsoleLogger('console_logger')
    file_logger = ConsoleLogger('file_logger')
    logger = Logger('logger')

    # Console Logger
    console_logger().info("** Testing ConsoleLogger Class **")
    console_logger().info("START")
    console_logger().debug('This is an example of a level of console_logger case of the type: debug')
    console_logger().info('This is an example of a level of console_logger case of the type: info')
    console_logger().warn('This is an example of a level of console_logger case of the type: warn')
    console_logger().error('This is an example of a level of console_logger case of the type: error')

    # File logger
    file_logger().info("** Testing FileLogger Class **")
    file_logger().info("START")
    file_logger().debug('This is an example of a level of file_logger case of the type: debug')
    file_logger().info('This is an example of a level of file_logger case of the type: info')
    file_logger().warn('This is an example of a level of file_logger case of the type: warn')
    file_logger().error('This is an example of a level of file_logger case of the type: error')

    # Logger
    logger().info("** Testing Logger Class **")
    logger().info("START")
    logger().debug('This is an example of a level of logger case of the type: debug')
    logger().info('This is an example of a level of logger case of the type: info')
    logger().warn('This is an example of a level of logger case of the type: warn')
    logger().error('This is an example of a level of logger case of the type: error')
