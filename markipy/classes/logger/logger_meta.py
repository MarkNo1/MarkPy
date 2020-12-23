from dataclasses import dataclass
from enum import Enum
from logging import Formatter, StreamHandler, FileHandler, Logger, LoggerAdapter

from markipy import DEFAULT_LOG_PATH
from ..path import Path
from ..base import BaseMeta


@dataclass
class LoggerMeta(BaseMeta):
    _class_name = 'LoggerMeta'

    class Mode(Enum):
        console = 1
        file = 2
        console_and_file = 3

    class Level(Enum):
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0

    _log_path: Path = DEFAULT_LOG_PATH
    _log_mode: Mode = Mode.console
    _log_level: Level = Level.DEBUG
    _log_rotation: str = 'd'

    _log_logger: Logger = None
    _log_console_handler: StreamHandler = None
    _log_file_handler: FileHandler = None
    # Final log to call
    log: LoggerAdapter = None

    _log_console_format: Formatter = Formatter(
        '[%(asctime)s] %(levelname).4s: [%(class_name)sV%(class_version)s]\t%(message)s')
    _log_file_format: Formatter = Formatter(
        '[%(asctime)s] <%(pathname)s-%(lineno)d> %(process)d %(levelname).4s: [%(class_name)sV%(class_version)s]\t%(message)s')

