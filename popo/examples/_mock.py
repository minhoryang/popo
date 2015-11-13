"""."""
from datetime import datetime
from enum import Enum


class Event(object):
    """."""

    class EventType(Enum):
        """."""
        Event_1 = 1
        Event_2 = 2
        Event_3 = 3

    id = 0
    type = EventType  # default: .Event_1
    username = ""  # max: 50
    results = []  # == List<Any>
    at = datetime.now()  # datetime, default: datetime.now

