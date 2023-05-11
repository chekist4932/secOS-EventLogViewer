from typing import Any

from pydantic import BaseModel


class LogModel(BaseModel):
    EventType: int | None
    TimeGenerated: Any
    SourceName: str
    EventID: int | None
    EventCategory: int | None

