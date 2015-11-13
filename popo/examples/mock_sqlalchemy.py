"""."""

# XXX : copied
from datetime import datetime
from enum import Enum

# TODO : imported for sqlalchemy
from sqlalchemy_utils import (
    ChoiceType,
    ScalarListType,
)
from . import db


# TODO : added additional for sqlalchemy
class EnumType(ChoiceType):
    def copy(self, **kargs):
        if 'schema' in kargs:
            kargs.pop('schema')
        return super(__class__, self).copy(**kargs)


# TODO : renamed with prefix('_') and postfix('MixIn')
class _EventMixIn(object):
    """."""   # XXX : copied

    class EventType(Enum):
        """."""
        Event_1 = "Event_1"  # TODO: overlapped numbering
        Event_2 = "Event_2"
        Event_3 = "Event_3"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(EnumType(EventType))
    username = db.Column(db.String(50))
    results = db.Column(ScalarListType(separator="\uFF0C"), default=[])
    at = db.Column(db.DateTime, default=datetime.now)


if __name__ == "__main__":
    # Use it like this
    class Event(_EventMixIn, db.Model):
        __bind_key__ = __tablename__ = "event"

