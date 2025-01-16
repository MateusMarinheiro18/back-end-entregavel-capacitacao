from pydantic import BaseModel, ConfigDict
from typing import Optional


class CreateEventDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    description: Optional[str] = ""
    location: str
    day: str
    month: str
    initial_time: str
    final_time: Optional[str] = ""
