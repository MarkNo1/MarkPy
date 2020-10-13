from pathlib import Path
from dataclasses import dataclass

from .process import Process

_rsync_ = {'class': 'Rsync', 'version': 2}


@dataclass
class Host:
    user: str
    ip: str
    path: Path

    def __str__(self):
        return f'{self.user}@{self.ip}:{self.path}'


class RsyncErrorOnlyOneCanBeRemote(Exception):
    def __init__(self, rsync):
        rsync.log.error('Only one from source or destination can be remote!')


class Rsync(Process):

    def __init__(self, source, destination, console=False):
        Process.__init__(self, 'Rsync-Sync', console=console)
        self._init_atom_register_class(_rsync_)
        self._check_input(source, destination)
        self.source = source
        self.destination = destination
        self.log.debug(self.ugrey(f'Initialized'))
        self.rsync_cmd = ['rsync', '-avzh', '--info=flist2,name,progress2']

    def sync(self):
        self.log.debug('Start sync')
        self.execute(self.rsync_cmd + [f'{self.source}', f'{self.destination}'])
        self.log.debug('End sync')

    def _check_input(self, source, destination):
        if isinstance(source, Host) and isinstance(destination, Host):
            raise RsyncErrorOnlyOneCanBeRemote(self)


def test_rsync():
    source = Path('/tmp/test/source/')
    destination = Host(user='mark', ip='10.168.72.103', path=Path('/tmp/test/destination/'))
    rsync = Rsync(source, destination)
    rsync.sync()
    source = Host('mark', '10.168.72.103', source)
    rsync = Rsync(source, destination)
    rsync.sync()
