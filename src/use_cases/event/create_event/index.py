from use_cases.event.create_event.create_event_dto import CreateEventDTO
from use_cases.event.create_event.create_event_use_case import CreateEventUseCase
from repositories.event_repository import EventRepository
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_event_use_case = CreateEventUseCase(EventRepository())

@router.post("/event")
def create_event(request: Request, response: Response, create_event_dto: CreateEventDTO):
    return create_event_use_case.execute(create_event_dto, response, request)
