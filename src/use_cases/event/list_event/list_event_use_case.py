from repositories.event_repository import EventRepository
from fastapi import Request, Response
from entities.event import Event
from typing import List

class ListEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, response: Response, request: Request) -> List[dict]:
        events = self.event_repository.get_all_events()
        if not events:
            response.status_code = 404
            return {"status": "error", "message":"Nenhum evento encontrado"}
        response.status_code = 200
        return events
    