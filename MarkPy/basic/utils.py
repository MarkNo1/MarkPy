from pathlib import Path
import wget

from .watchdog import WatchFolder

DEFAULT_UTILS_INSTALL = '/mark/utils'


class PycharmDownloader (WatchFolder):
    _url : str = 'https://download.jetbrains.com/python/pycharm-community-2020.2.2.tar.gz'
    _path : Path = Path(DEFAULT_UTILS_INSTALL)
    _filename : Path = Path('._mark_utils_pycharm_')

    def dowload(self):
        self. _filename = wget.download(self._url)
