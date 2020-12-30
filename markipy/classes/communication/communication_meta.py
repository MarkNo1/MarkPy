from dataclasses import dataclass
from threading import Lock

from ..base import safe_init_meta_class


@dataclass(unsafe_hash=True, init=False)
class CommunicationMeta:
    _com_channel: object = None
    _com_buffer_size: int = 15000
    _com_completed: bool = False
    _com_n_publisher: int = 1
    _com_n_subscriber: int = 1
    _com_publisher_completed: int = 0
    _com_producer_lock = Lock()

    def __init__(self, **kwargs):
        safe_init_meta_class(self, kwargs)
