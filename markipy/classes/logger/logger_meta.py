import dataclasses
from enum import Enum
from logging import Formatter, StreamHandler, FileHandler, Logger, LoggerAdapter
from random import randint

from markipy import DEFAULT_LOG_PATH
from ..path import Path
from ..base import safe_init_meta_class


@dataclasses.dataclass(unsafe_hash=True, init=False)
class LoggerMeta:
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
    _log_file_name: str = 'LoggerMeta.log'

    _log_logger: Logger = None
    _log_console_handler: StreamHandler = None
    _log_file_handler: FileHandler = None

    # Final logger to call
    log: LoggerAdapter = None

    _log_console_format: Formatter = Formatter(
        '%(asctime)s <%(class_name)s> %(levelname).4s: \t%(message)s')
    _log_file_format: Formatter = Formatter(
        '%(asctime)s <%(pathname)s-%(lineno)d> %(process)d <%(class_name)s> %(levelname).4s:\t%(message)s')

    _log_rnd_id: int = randint(0, 1000)

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
