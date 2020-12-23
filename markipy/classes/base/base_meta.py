from dataclasses import dataclass

from ..time import Time
from ..path import Path


@dataclass
class BaseMeta:
    _class_name: str = 'BaseMeta'
    _class_version: str = '0.0.1'
    _class_creation_date: str = Time.now()
    _class_deletion_date: str = "nan"
    _class_creation_path: Path = Path().cwd()
    _class_working_path: Path = Path.cwd()
