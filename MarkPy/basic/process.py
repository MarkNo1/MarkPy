from pathlib import Path
import subprocess

from .logger import Logger


class Process(Logger):

    __process_version__ = 1

    def __init__(self, processName, path=Path.cwd()):
        Logger.__init__(self, f'.process_{processName}.log', path=path)
        self.newLogAtom('Process', self.__process_version__)
        self.proc = None
        self.initialized()

    def run(self, cmd):
        self.log.debug('Process start')
        self.proc = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding='utf-8')
        while True:
            line = self.proc.stdout.readline()
            self.log.debug(line)
            if line == '' and self.proc.poll() != None:
                break
            self.log.debug('Process completed')

    def __del__(self):
        Logger.__del__(self)
