from typing import Any

from pydantic import BaseModel


class LogSchema(BaseModel):
    EventType: str
    TimeGenerated: str
    SourceName: str
    EventID: str
    EventCategory: str

