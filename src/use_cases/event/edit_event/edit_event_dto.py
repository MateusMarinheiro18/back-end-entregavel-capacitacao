from pydantic import BaseModel, Field

class EditEventDTO(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=255)
    location: str = Field(..., max_length=100)
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    initial_time: str
    final_time: str
