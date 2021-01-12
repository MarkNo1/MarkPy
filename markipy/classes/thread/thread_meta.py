from dataclasses import dataclass

from ..communication import Communication
from ..base import safe_init_meta


@dataclass(init=False, unsafe_hash=True)
class ThreadMeta:
    _thread_name: str = 'Thread'
    _thread_daemon: bool = True
    _thread_com_channel: Communication = None
    _thread_com_block: bool = True
    _thread_com_block_timeout: int = 7
    _thread_completed: bool = False

    def __init__(self, **kwargs):
        safe_init_meta(self, kwargs)
