import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Event(BaseModel):
    _id: str
    name: str
    description: Optional[str]
    location: str
    day: str
    month: str
    initial_time: str
    final_time: Optional[str]