from fastapi import APIRouter, Depends, HTTPException
from use_cases.edit_event_use_case import EditEventUseCase
from repositories.event_repository import EventRepository
from dtos.edit_event_dto import EditEventDTO


router = APIRouter()

# Instancia o repositório e o use case
event_repository = EventRepository()
edit_event_use_case = EditEventUseCase(event_repository)

@router.put("/events/{event_id}")
def edit_event(event_id: str, event_data: EditEventDTO):
    try:
        result = edit_event_use_case.execute(event_id, event_data.dict())
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao editar evento")
