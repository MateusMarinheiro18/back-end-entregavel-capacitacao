from repositories.event_repository import EventRepository
from fastapi import Request, Response
from datetime import datetime

class GetEventByIdUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, event_id: str, response: Response):
        event = self.event_repository.get_event_by_id(event_id)
        if not event:
            response.status_code = 404
            return {"message": "Event not found"}
        return event