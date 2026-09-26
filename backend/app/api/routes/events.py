from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.event import EventRecord
from app.services.event_service import EventService

router = APIRouter(tags=["events"])


class EventCreateRequest(BaseModel):
    source: str
    event_type: str
    data: dict = {}


@router.get("/events")
async def list_events():
    return await EventService.list_events()


@router.post("/events", status_code=201)
async def create_event(payload: EventCreateRequest):
    if not payload.source or not payload.event_type:
        raise HTTPException(status_code=400, detail="source and event_type are required")

    event = EventRecord(
        source=payload.source,
        event_type=payload.event_type,
        data=payload.data,
    )
    created = await EventService.capture_event(event)
    return created
