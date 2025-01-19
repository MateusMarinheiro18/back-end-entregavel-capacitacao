from fastapi import APIRouter, HTTPException
from typing import List
from use_cases.event.calendar_event.calendar_event_use_case import CalendarEventUseCase
from use_cases.event.calendar_event.calendar_event_dto import CalendarEventDTO

router = APIRouter()
calendar_event_use_case = CalendarEventUseCase()

@router.get("/calendar-events", response_model=List[CalendarEventDTO])
def list_events():
    try:
        print('cheguei aqui')
        events = calendar_event_use_case.get_all_events()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar eventos: {e}")

@router.get("/calendar-events/{day}/{month}", response_model=List[CalendarEventDTO])
def filter_events(day: str, month: str):
    try:
        events = calendar_event_use_case.get_events_by_day_and_month(day, month)
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao filtrar eventos: {e}")
