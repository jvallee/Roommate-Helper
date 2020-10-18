import datetime

import mongoengine


class FoodItem(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    dateBought = mongoengine.DateTimeField(default=datetime.datetime.now)
    dataExpire = mongoengine.DateTimeField(default=datetime.datetime.now)