from pathlib import Path

from .process import Process


class Host():
    def __init__(self, user, ip, path):
        self.user = user
        self.ip = ip
        self.path = path

    def __str__(self):
        return f'{user}@{ip}:{path}'


class Rsync(Process):

    __rsync_version = 2

    def __init__(self, source, destination, path=Path.cwd()):
        Process.__init__(self,'Rsync-Sync', path=path)
        self.newLogAtom('Rsync', self.__rsync_version)
        self.source = source
        self.destination = destination
        self.initialized()
        self.rsync_cmd = 'rsync -avzh --info=flist2,name,progress2'

    def sync(self):
        self.log.debug('Start sync')
        self.run(self.rsync_cmd + f'{self.source} {self.destination}')
        self.log.debug('End sync')
