# index delete_event
from fastapi import APIRouter, Depends, HTTPException, Response

from use_cases.event.delete_event.delete_event_use_case import DeleteEventUseCase
from repositories.event_repository import EventRepository

router = APIRouter()
event_repository = EventRepository()
delete_event_use_case = DeleteEventUseCase(event_repository)

@router.delete("/events/{event_id}")
def delete_event(event_id: str, response: Response):
    return delete_event_use_case.execute(event_id, response)