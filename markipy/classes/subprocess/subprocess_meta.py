from dataclasses import dataclass
from subprocess import Popen

from ..communication import Communication
from ..base import safe_init_meta_class


@dataclass(init=False, unsafe_hash=True)
class SubProcessMeta:
    _process_name: str = 'Thread'
    _process_cmd: str = ''
    _process_proc: Popen = None
    _process_com_channel: Communication = None
    _process_wait_timeout: int = None
    _process_completed: bool = False

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
