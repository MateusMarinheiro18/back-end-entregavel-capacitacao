from fastapi import APIRouter, Depends, HTTPException, Response
from use_cases.event.edit_event.edit_event_use_case import EditEventUseCase
from repositories.event_repository import EventRepository
from use_cases.event.edit_event.edit_event_dto import EditEventDTO


router = APIRouter()

# Instancia o repositório e o use case
event_repository = EventRepository()
edit_event_use_case = EditEventUseCase(event_repository)

@router.post("/event-edit/{event_id}")
def edit_event(event_id: str, event_data: EditEventDTO, response: Response):
    print('cheguei aqui')
    result = edit_event_use_case.execute(event_id, event_data.dict())
    return result
