from dataclasses import dataclass
from subprocess import PIPE, Popen
import shlex

from .subprocess_meta import SubProcessMeta
from .subprocess_exceptions import SubProcessException
from ..logger import Logger


def clean_process_stdout_line(line):
    return str(line).replace('\r', '').replace('\n', '')


@dataclass(init=False, unsafe_hash=True)
class SubProcess(Logger, SubProcessMeta):
    _class_name = 'SubProcess'

    def __init__(self, **kwargs):
        Logger.__init__(self, **kwargs)
        SubProcessMeta.__init__(self, **kwargs)

        if self._process_cmd == '':
            raise SubProcessException.EmptyCommandPassed(self)

    def _process_execute(self):
        self._process_cmd = shlex.split(self._process_cmd)
        self._process_proc = Popen(args=self._process_cmd, bufsize=1, cwd=self._class_working_path, stdout=PIPE,
                                   stderr=PIPE,
                                   universal_newlines=True)
        for line in self._process_proc.stdout:
            if self._process_com_channel is not None:
                self._process_com_channel.send(clean_process_stdout_line(line))

    def start(self):
        self._process_execute()
        self._set_process_completed()

    def _set_process_completed(self):
        self._process_completed = True
        self._process_proc.stdout.close()
        self._process_proc.stderr.close()

    def join(self):
        self._process_proc.wait(timeout=self._process_wait_timeout)


