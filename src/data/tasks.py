from datetime import datetime
from datetime import timedelta
import mongoengine


class Task(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    registered_date = mongoengine.DateTimeField(default=datetime.now)
    lastCompleted = mongoengine.DateTimeField(default=datetime.now)
    nextDue = mongoengine.DateTimeField()
    periodLengthInDays = mongoengine.IntField()
    assignedTo = mongoengine.StringField()
