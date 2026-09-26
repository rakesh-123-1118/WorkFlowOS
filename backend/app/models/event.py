from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, Field


class EventRecord(BaseModel):
    event_id: Optional[str] = None
    source: str
    event_type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    data: dict[str, Any] = Field(default_factory=dict)
