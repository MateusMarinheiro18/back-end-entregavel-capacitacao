from use_cases.event.list_event.list_event_use_case import ListEventUseCase
from repositories.event_repository import EventRepository
from fastapi import Request, Response, APIRouter

router = APIRouter()

list_event_use_case = ListEventUseCase(EventRepository())

@router.get("/event")
def list_event(response: Response, request: Request):
    return list_event_use_case.execute(response, request)
