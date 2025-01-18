# delete event use case
from fastapi import APIRouter, Depends, HTTPException, Response
from repositories.event_repository import EventRepository

class DeleteEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, event_id: str, response: Response):
        try:
            return self.event_repository.delete_event(event_id)
        except Exception as e:
            response.status_code = 400
            return {"message": str(e)}