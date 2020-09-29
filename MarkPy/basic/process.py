from pathlib import Path
import asyncio
from asyncio.subprocess import PIPE

from .logger import Logger


class Process(Logger):

    __process_version__ = 1

    def __init__(self, processName, path=Path.cwd()):
        Logger.__init__(self, f'.process_{processName}.log', path=path)
        self.newLogAtom('Process', self.__process_version__)
        self.proc = None
        self.initialized()

    def _clean_out_line(self, line):
        return str(line,'utf-8').replace('\r', '').replace('\n','')

    async def _read_stream(self, stream, cb):
        while True:
            line = await stream.readline()
            if line:
                cb(self._clean_out_line(line))
            else:
                break

    async def _stream_subprocess(self, cmd):
        process = await asyncio.create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)
        await asyncio.wait([
            self._read_stream(process.stdout, self.log.debug),
            self._read_stream(process.stderr, self.log.error)
        ])
        return await process.wait()

    def execute(self, cmd):
        self.log.debug(f'Process executing: {self.cyan(cmd)}')
        loop = asyncio.get_event_loop()
        rc = loop.run_until_complete( self._stream_subprocess(cmd) )
        loop.close()
        self.log.debug('Process completed')
        return rc

    def __del__(self):
        Logger.__del__(self)


def test_process():
    p = Process('test')
    p.execute(['ls','-a'])
