from repositories.event_repository import EventRepository
from fastapi import Request, Response
from datetime import datetime

class GetEventsByDateUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, start_date: str, end_date: str, response: Response):
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            events = self.event_repository.get_events_by_date_range(start_date, end_date)
            response.status_code = 200
            return {"status": "success", "events": [event.to_mongo() for event in events]}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": str(e)}
