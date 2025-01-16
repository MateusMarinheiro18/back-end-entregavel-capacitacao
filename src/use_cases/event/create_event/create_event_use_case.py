from repositories.event_repository import EventRepository
from use_cases.event.create_event.create_event_dto import CreateEventDTO 
from fastapi import Request, Response
from entities.event import Event

class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, create_event_dto: CreateEventDTO, response: Response, request: Request):
        if not create_event_dto.name or not create_event_dto.description or not create_event_dto.location or not create_event_dto.day or not create_event_dto.month or not create_event_dto.initial_time or not create_event_dto.final_time:
            response.status_code = 407
            return {"status": "error", "message":"faltam informações"}

        event = Event(
            name=create_event_dto.name,
            description=create_event_dto.description,
            location=create_event_dto.location,
            day= create_event_dto.day,
            month= create_event_dto.month,
            initial_time=create_event_dto.initial_time,
            final_time=create_event_dto.final_time
        )

        self.event_repository.save(event)
        response.status_code=400
        return {"status": "success", "message":"Evento criado"}
