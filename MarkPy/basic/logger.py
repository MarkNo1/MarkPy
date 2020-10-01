from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
from datetime import date

from .style import Style

DEFAULT_LOG_PATH = Path('/var/MarkPy/')

class BaseLogger(Style):
    __base_logger_version__ = 3
    __hasBaseLogger__ = False

    def __init__(self, loggerName, level=logging.DEBUG):
        if not self.__hasBaseLogger__:
            Style.__init__(self)
            self.newAtom(self.sequential('BaseLogger'), self.sequential(self.__base_logger_version__))
            self.next_sequential()
            # Logger
            self.__logger__ = logging.getLogger(loggerName)
            # Set Level
            self.__logger__.setLevel(level)
            # Do not re-init
            self.__hasBaseLogger__ = True

    def newLogAtom(self, atom_name, atom_version):
        self.newAtom(self.sequential(atom_name), self.sequential(atom_version))
        self.next_sequential()
        self.log = logging.LoggerAdapter(self.__logger__ , dict(atom_name=self.__name__, atom_version=self.__version__))

    def _set_format(self):
        return Formatter('''[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d\n|%(atom_version)s|%(atom_name)s %(levelname).4s:\t%(message)s''')

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
    __console_logger_version__ = 3
    def __init__(self, loggerName='ConsoleLogger', level=logging.DEBUG):
        BaseLogger.__init__(self, loggerName, level)
        self.newLogAtom('ConsoleLogger', self.__console_logger_version__)
        # Logger
        if not self.__logger__.hasHandlers():
            self.__console_handler__ = logging.StreamHandler()
            self.__console_handler__.setFormatter(self._set_format())
            self.__logger__.addHandler(self.__console_handler__)

        self.log.debug(self.ugrey(f'Initialized'))

    def __del__(self):
        BaseLogger.__del__(self)


class FileLogger(BaseLogger):
    __file_logger_version__ = 5
    def __init__(self, log_file, loggerName='FileLogger', level=logging.DEBUG, rotation = 'd'):
        BaseLogger.__init__(self, level)
        self.newLogAtom('FileLogger', self.__file_logger_version__)
        # Logger
        self.__file_handler__ = logging.handlers.TimedRotatingFileHandler(log_file, when=rotation , backupCount=5)
        self.__file_handler__.setFormatter(self._set_format())
        self.__logger__.addHandler(self.__file_handler__)
        self.log.debug(self.ugrey(f'Initialized'))
        self.log.debug(f'Logging on: {self.orange(log_file)}')

    def __del__(self):
        BaseLogger.__del__(self)

class Logger(ConsoleLogger, FileLogger):
    __logger_version__ = 7

    def __init__(self, loggerName='Logger', logPath=DEFAULT_LOG_PATH, level=logging.DEBUG):
        if 'ConsoleLogger' not in self.__name__:
            ConsoleLogger.__init__(self, loggerName, level)
        if 'FileLogger' not in self.__name__:
            FileLogger.__init__(self, Path(logPath) / f'{loggerName}.{date.today()}.log', loggerName , level)
        self.newLogAtom('Logger', self.__logger_version__ )
        self.log.debug(self.ugrey(f'Initialized'))

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
    console_logger().error(console_logger.error('This is an example of a level of console_logger case of the type: error with style'))
    console_logger().info(console_logger.highlight('This is an example of a level of console_logger case of the type: info with style'))
    console_logger().warn(console_logger.warning('This is an example of a level of console_logger case of the type: warn with style'))

    # File logger
    file_logger().info("** Testing FileLogger Class **")
    file_logger().info("START")
    file_logger().debug('This is an example of a level of file_logger case of the type: debug')
    file_logger().info('This is an example of a level of file_logger case of the type: info')
    file_logger().warn('This is an example of a level of file_logger case of the type: warn')
    file_logger().error('This is an example of a level of file_logger case of the type: error')
    file_logger().error(file_logger.error('This is an example of a level of file_logger case of the type: error with style'))
    file_logger().info(file_logger.highlight('This is an example of a level of file_logger case of the type: info with style'))
    file_logger().warn(file_logger.warning('This is an example of a level of file_logger case of the type: warn with style'))

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
