from fastapi import APIRouter, Request, Response
from .get_events_by_id_use_case import GetEventByIdUseCase
from repositories.event_repository import EventRepository

router = APIRouter()
event_repository = EventRepository()
get_event_by_id_use_case = GetEventByIdUseCase(event_repository)

@router.get("/event-get/{event_id}")
def get_event(event_id: str, response: Response):
    return get_event_by_id_use_case.execute(event_id, response)
