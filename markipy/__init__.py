from pathlib import Path
from os import makedirs

# DEFAULT PACKAGE FOLDER
_markipy_default_package_dir = Path().home() / '.markipy'
_unittest_default_dir = '/tmp/unittest'
_log_default_dir = _markipy_default_package_dir / 'logs'

makedirs(_unittest_default_dir, exist_ok=True)
makedirs(_log_default_dir, exist_ok=True)

from . import classes

# from . import basic
# from . import script
# from . import gui
