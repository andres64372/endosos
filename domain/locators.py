import dataclasses
from typing import List

from utils.dataclass_classmethods import FromDictMixin
from .record_locator import RecordLocator

@dataclasses.dataclass
class Locators(FromDictMixin):
    numeric_record_locator: str = None
    parent_record_locator: str = None
    parent_id: int = 0
    record_locators: List[RecordLocator] = dataclasses.field(default_factory=list)