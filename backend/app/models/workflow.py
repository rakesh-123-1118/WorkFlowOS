from datetime import datetime, timezone
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


class WorkflowEvent(BaseModel):
    event_id: str
    source: str
    event_type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    data: dict[str, Any] = Field(default_factory=dict)


class WorkflowStep(BaseModel):
    type: Literal["trigger", "action", "condition", "notification"]
    name: str
    description: str
    config: dict[str, Any] = Field(default_factory=dict)
    order: int


class Workflow(BaseModel):
    workflow_id: Optional[str] = None
    name: str
    description: str
    intent: str
    status: Literal["draft", "approved", "active", "paused", "archived"] = "draft"
    triggers: list[dict[str, Any]] = Field(default_factory=list)
    steps: list[WorkflowStep] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
