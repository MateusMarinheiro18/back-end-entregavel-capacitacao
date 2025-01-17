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
    
    def get_all_events(self) -> List[dict]:
        events = EventModel.objects()
        events_dict = [event.to_mongo().to_dict() for event in events]
        for event in events_dict:
            event['_id'] = str(event['_id'])
        return events_dict
    
    def update_event(self, event_id: str, data: dict) -> None:
        event = EventModel.objects.with_id(event_id)
        if not event:
            return None
        for k in data:
            if (k in EventModel.get_normal_fields()):
                event[k] = data[k]
            elif (k in EventModel.sensivity_fields):
                event[k] = SensivityField(fernet=self.fernet, data=data[k])
        event.save()
        return None
    
    def delete_event(self, event_id: str) -> None:
        event = EventModel.objects.with_id(event_id)
        if not event:
            return None
        event.delete()
        return None
    