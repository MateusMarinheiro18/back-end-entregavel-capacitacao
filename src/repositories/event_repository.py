import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.event import Event
from models.event_model import EventModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class EventRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, event: Event) -> None:
        event_model = EventModel()
        event_dict = event.model_dump()

        for k in EventModel.get_normal_fields():
            if (k not in event_dict):
                continue

            event_model[k] = event_dict[k]

        for k in EventModel.sensivity_fields:
            event_model[k] = SensivityField(fernet=self.fernet, data=event_dict[k])

    

        event_model.save()

        return None
    
    def get_event_by_id(self, event_id: str) -> dict:
        event = EventModel.objects.with_id(event_id)
        if not event:
            return None
        event_dict = event.to_mongo().to_dict()
        event_dict['_id'] = str(event_dict['_id'])
        return event_dict