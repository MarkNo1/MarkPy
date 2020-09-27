from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

from .atom import Atom


class BaseLogger(Atom):

    __hasBaseLogger__ = False

    def __init__(self, level=logging.DEBUG):
        Atom.__init__(self, 'BaseLogger', self.__class__)
        if not self.__hasBaseLogger__:
            # Logger
            self.__logger__ = logging.getLogger(self.__name__)
            # Set Level
            self.__logger__.setLevel(level)
            # Do not re-init
            self.__hasBaseLogger__ = True

    def registerAtom(self, atom_name, atom_version):
        self.newAtom(atom_name, atom_version)
        self.log = logging.LoggerAdapter(self.__logger__ , dict(atom_name=self.__name__, atom_version=self.__version__))

    def _set_format(self):
        return Formatter('''{<%(pathname)s-%(lineno)d>%(process)d<%(atom_name)s-v%(atom_version)s> \t%(levelname).4s\t%(asctime)s:\t%(message)s''')


    def __call__(self):
        return self.log


class ConsoleLogger(BaseLogger):
    __console_logger_version__ = 3
    def __init__(self, level=logging.DEBUG):
        BaseLogger.__init__(self, level)
        self.registerAtom('Console', self.__console_logger_version__)
        # Logger
        if not self.__logger__.hasHandlers():
            self.__console_handler__ = logging.StreamHandler()
            self.__console_handler__.setFormatter(self._set_format())
            self.__logger__.addHandler(self.__console_handler__)


class FileLogger(BaseLogger):
    __file_logger_version__ = 5
    def __init__(self, log_file, level=logging.DEBUG, rotation = 'd'):
        BaseLogger.__init__(self, level)
        self.registerAtom('File', self.__file_logger_version__)
        # Logger
        self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(log_file, when=rotation , backupCount=5)
        self.__file_handler__.setFormatter(self._set_format())
        self.__logger__.addHandler(self.__file_handler__)


class Logger(ConsoleLogger, FileLogger):
    __logger_version__ = 6
    def __init__(self, file=None, level=logging.DEBUG):
        ConsoleLogger.__init__(self, level)
        FileLogger.__init__(self, Path(file) if file else Path.cwd() / Path(f'{file}.log'), level)
        self.registerAtom('Logger', self.__logger_version__ )



def test_logger():
    console_logger = ConsoleLogger()
    file_logger = FileLogger('FileLogger.test')
    logger = Logger()

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
