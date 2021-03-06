from mongoengine import *
from django.conf import settings

connect(settings.X())

class User(Document):
    firstname = StringField(max_length=32, required=True)
    lastname = StringField(max_length=32, required=True)
    email = StringField(max_length=128, required=True)
    password = StringField(max_length=32, required=True)
