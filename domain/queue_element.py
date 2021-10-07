import dataclasses

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class QueueElement(FromDictMixin):
    booking_queue_item_key: str = None
    process_status: int = 0
    segment_key: str = None
    process_state: int = 0
    watch_list_id: str = None
    in_progress: bool = False
    passenger_id: str = None
    status_reset: str= None
    domain_code: str = None
    note: str = None
    passenger_name: str = None
    priority_date: str = None
    event_type: int = 0
    restriction: int = 0
    record_locator: str = None