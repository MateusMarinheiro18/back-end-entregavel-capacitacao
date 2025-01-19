from typing import List
from repositories.event_repository import EventRepository
from entities.event import Event

class CalendarEventUseCase:
    def __init__(self):
        self.event_repository = EventRepository()

    def get_all_events(self) -> List[Event]:
        print("Getting")
        """Retorna todos os eventos do calendário diretamente do banco de dados."""
        return self.event_repository.get_all_events()

    def get_events_by_day_and_month(self, day: str, month: str) -> List[Event]:
        """Retorna os eventos de um dia e mês específicos do banco de dados."""
        return self.event_repository.get_by_day_and_month(day, month)
