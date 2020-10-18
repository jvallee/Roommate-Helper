import mongoengine


class User(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True, unique=True)
    apartment_ids = mongoengine.ListField()
    password = mongoengine.StringField(required=True)
    favorite_apartment = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
