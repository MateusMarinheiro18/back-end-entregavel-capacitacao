from pydantic import BaseModel
from typing import Optional

class CalendarEventDTO(BaseModel):
    _id: str
    name: str
    description: Optional[str]
    location: str
    day: str
    month: str
    initial_time: str
    final_time: Optional[str]
