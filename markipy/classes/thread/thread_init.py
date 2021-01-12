import threading
from dataclasses import dataclass

from .thread_abc import ThreadABC


@dataclass(init=False, unsafe_hash=True)
class ThreadInit(ThreadABC, threading.Thread):

    def __init__(self, **kwargs):
        ThreadABC.__init__(self, **kwargs)
        threading.Thread.__init__(self)
