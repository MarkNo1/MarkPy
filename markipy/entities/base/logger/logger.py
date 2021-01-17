import logging
from logging import Formatter, StreamHandler, FileHandler, Logger, LoggerAdapter
from logging import StreamHandler, LoggerAdapter
from logging.handlers import TimedRotatingFileHandler

from dataclasses import dataclass
from enum import Enum
from random import randint
import emoji

from markipy import _log_default_dir, makedirs
from ..class_meta import ClassMeta
from ..path import Path


def colorize(color_code, text):
    return f'\x1b[%sm{text}\x1b[0m' % (color_code)


def colorcode(a, b, c):
    return f'{a};{b};{c}'


def get_color_table():
    return [colorcode(a, b, c)
            for a in range(8)
            for b in range(38)
            for c in range(48)]


def get_emoji_table():
    return [emo for name, emo in emoji.unicode_codes.EMOJI_UNICODE.items()]


COLOR_TABLE = get_color_table()
EMOJI_TABLE = get_emoji_table()


def has_logger_class(cls):
    return hasattr(cls, 'log')


@dataclass(init=False, unsafe_hash=True)
class Logger(ClassMeta):
    _class_log_path: Path = _log_default_dir

    class LoggerMode(Enum):
        console = 1
        file = 2
        console_and_file = 3
        shared_logger = 4

    class LoggerLevel(Enum):
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0

    _log_mode: LoggerMode = LoggerMode.console
    _log_level: LoggerLevel = LoggerLevel.DEBUG
    _log_rotation: str = 'd'
    _log_file_path: Path = None

    _log_logger: Logger = None
    _log_console_handler: StreamHandler = None
    _log_file_handler: FileHandler = None

    _log_if_exist_use_it: bool = True

    # Final logger to call
    log: LoggerAdapter = None

    _log_console_format: Formatter = Formatter(
        '%(asctime)s <%(class_name)s> %(levelname).4s: \t%(message)s')
    _log_file_format: Formatter = Formatter(
        '%(asctime)s <%(pathname)s-%(lineno)d> %(process)d <%(class_name)s> %(levelname).4s:\t%(message)s')

    _log_colors = COLOR_TABLE
    _log_colors_len = len(_log_colors)

    _log_emoji = EMOJI_TABLE
    _log_emoji_len = len(_log_emoji)

    _log_rnd_id: int = randint(0, 1000)

    def __init__(self, **kwargs):
        ClassMeta.__init__(self, **kwargs)

        self._safe_init_(kwargs)

        if not Path(self._class_log_path).exists():
            makedirs(self._class_log_path, exist_ok=True)

        if self._log_file_path is None:
            self._log_file_path = Path(self._class_log_path) / Path(f'{self._class_name}.log')

        if self._log_if_exist_use_it:
            if has_logger_class(self) and self._log_logger is not None:
                self._log_mode = self.LoggerMode.shared_logger

        # Console Logger
        if self._log_mode == self.LoggerMode.console:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File Logger
        if self._log_mode == self.LoggerMode.file:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_file_handler = TimedRotatingFileHandler(self._log_file_path, when=self._log_rotation, interval=1,
                                                              backupCount=5)
            self._log_file_handler.doRollover()
            self._log_file_handler.setFormatter(self._log_file_format)
            self._log_logger.addHandler(self._log_file_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File and Console Logger
        if self._log_mode == self.LoggerMode.console_and_file:
            self._log_logger = logging.getLogger(str(hash(self)))
            self._log_logger.setLevel(self._log_level.value)
            self._log_console_handler = StreamHandler()
            self._log_console_handler.setFormatter(self._log_console_format)
            self._log_logger.addHandler(self._log_console_handler)
            self._log_file_handler = TimedRotatingFileHandler(self._log_file_path,
                                                              when=self._log_rotation, interval=1, backupCount=5)
            self._log_file_handler.doRollover()
            self._log_file_handler.setFormatter(self._log_file_format)
            self._log_logger.addHandler(self._log_file_handler)
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

        # File logger from already exist Logger
        if self._log_mode == self.LoggerMode.shared_logger:
            self.log = LoggerAdapter(self._log_logger, dict(class_name=self._class_name))

    def share_logger(self) -> dict:
        shared = dict(_log_mode=self.LoggerMode.shared_logger)
        for k, v in self.__dict__.items():
            if '_log' in k and 'mode' not in k:
                shared.update({k: v})
        return shared

    def color(self, color_id, text):
        return colorize(self._log_colors[color_id], text)

    def emoji(self, emoji_id):
        return self._log_emoji[emoji_id]

    def print_all_colors(self):
        colors = ''
        for i in range(self._log_colors_len):
            if i % 10 == 0:
                colors += '\n'
            colors += f' {self.color(i, str(i))}'
        print(colors)

    def print_all_emoji(self):
        emoticon = ''
        for i, e in enumerate(self._log_emoji):
            if i % 5 == 0:
                emoticon += '\n'
            emoticon += f'\t{i}: {e}'
        print(emoticon)

    def red(self, text):
        return self.color(79, text)

    def green(self, text):
        return self.color(80, text)

    def orange(self, text):
        return self.color(33, text)

    def yellow(self, text):
        return self.color(81, text)

    def blue(self, text):
        return self.color(82, text)

    def violet(self, text):
        return self.color(35, text)

    def cyan(self, text):
        return self.color(84, text)

    def light_violet(self, text):
        return self.color(93, text)

    def lightblue(self, text):
        return self.color(36, text)

    def grey(self, text):
        return self.color(4782, text)

    def bred(self, text):
        return self.color(41, text)

    def bold_green(self, text):
        return self.color(42, text)

    def bold_orange(self, text):
        return self.color(43, text)

    def bold_blue(self, text):
        return self.color(44, text)

    def bold_violet(self, text):
        return self.color(45, text)

    def bold_lightblue(self, text):
        return self.color(46, text)

    def underline_grey(self, text):
        return self.color(11954, text)

    def mark(self):
        return self.emoji(3086)

    def denied(self):
        return self.emoji(2169)

    def error(self, text):
        return self.red(text)

    def success(self, text):
        return self.green(text)

    def warning(self, text):
        return self.orange(text)

    def highlight(self, text):
        return self.blue(text)
