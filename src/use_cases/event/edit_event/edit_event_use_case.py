from repositories.event_repository import EventRepository
from entities.event import Event
from fastapi import HTTPException
from typing import Dict

class EditEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, event_id: str, data: Dict):
        # Verifica se o evento existe
        event = self.event_repository.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        # Atualiza os campos do evento
        updated_data = {
            "name": data.get("name"),
            "description": data.get("description"),
            "location": data.get("location"),
            "day": data.get("day", event),
            "month": data.get("month"),
            "initial_time": data.get("initial_time",),
            "final_time": data.get("final_time"),
        }



        # Atualiza o evento no repositório
        self.event_repository.update_event(event_id, updated_data)

        return {"status": "success", "message": "Evento atualizado com sucesso"}
