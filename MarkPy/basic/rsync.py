from pathlib import Path

from .process import Process


class Host():
    def __init__(self, user, ip, path):
        self.user = user
        self.ip = ip
        self.path = path

    def __str__(self):
        return f'{self.user}@{self.ip}:{self.path}'



class Rsync(Process):

    __rsync_version__ = 2

    def __init__(self, source, destination, path=Path.cwd()):
        Process.__init__(self,'Rsync-Sync', path=path)
        self.newLogAtom('Rsync', self.__rsync_version__)
        self.source = source
        self.destination = destination
        self.initialized()
        self.rsync_cmd = ['rsync', '-avzh', '--info=flist2,name,progress2']

    def sync(self):
        self.log.debug('Start sync')
        self.execute( self.rsync_cmd + [ f'{self.source}', f'{self.destination}'])
        self.log.debug('End sync')


def test_rsync():
    source = Path('/tmp/test/source/')
    destination = Host('mark', '172.23.87.156', '/tmp/test/destination/')
    rsync = Rsync(source, destination)
    rsync.sync()
