from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class EventModel(Document):
    sensivity_fields = [        
    ]

    name = StringField(required=True)
    description = StringField()
    location = StringField(required=True)
    day = StringField(required=True)
    month = StringField(required=True)
    initial_time = StringField(required=True)
    final_time = StringField()

    def get_normal_fields():
        return [i for i in EventModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in EventModel.sensivity_fields]
