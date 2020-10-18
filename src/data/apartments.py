import datetime
import mongoengine

from data.tasks import Task


class Apartment(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    occupants = mongoengine.ListField()
    tasks = mongoengine.EmbeddedDocumentListField(Task)
    apartmentName = mongoengine.StringField(required=True)
    user_ids = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'apartments'
    }
