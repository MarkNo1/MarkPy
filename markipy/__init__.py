from pathlib import Path

from . import basic
from . import script
from . import gui

# DEFAULT PACKAGE FOLDER
DEFAULT_PACKAGE_FOLDER = Path().home() / '.markipy'
DEFAULT_LOG_PATH = DEFAULT_PACKAGE_FOLDER / 'logs'

if not DEFAULT_LOG_PATH.exists():
    DEFAULT_LOG_PATH.mkdir()
