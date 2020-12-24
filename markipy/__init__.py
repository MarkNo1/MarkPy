from pathlib import Path
from os import makedirs


def ensure_folder(folder: Path):
    if not folder.exists():
        makedirs(folder, exist_ok=True)


# DEFAULT PACKAGE FOLDER
DEFAULT_PACKAGE_FOLDER = Path().home() / '.markipy'
DEFAULT_UNITTEST_FOLDER = DEFAULT_PACKAGE_FOLDER / 'unittest'
DEFAULT_LOG_PATH = DEFAULT_PACKAGE_FOLDER / 'logs'

ensure_folder(DEFAULT_PACKAGE_FOLDER)
ensure_folder(DEFAULT_UNITTEST_FOLDER)
ensure_folder(DEFAULT_LOG_PATH)

from . import basic
from . import script
from . import gui
from . import classes