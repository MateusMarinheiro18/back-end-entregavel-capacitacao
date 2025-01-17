from fastapi import APIRouter, Request, Response
from .get_events_by_date_use_case import GetEventsByDateUseCase
from repositories.event_repository import EventRepository

router = APIRouter()
event_repository = EventRepository()
get_events_by_date_use_case = GetEventsByDateUseCase(event_repository)

@router.get("/calendar/events")
def get_events_by_date(start_date: str, end_date: str, response: Response):
    return get_events_by_date_use_case.execute(start_date, end_date, response)
