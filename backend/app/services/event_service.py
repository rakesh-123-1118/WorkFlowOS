from app.db.mongo import mongo_db
from app.models.event import EventRecord


class EventService:
    collection = mongo_db["events"]

    @staticmethod
    async def capture_event(event: EventRecord):
        payload = event.model_dump()
        result = await EventService.collection.insert_one(payload)
        payload["event_id"] = str(result.inserted_id)
        await EventService.collection.update_one(
            {"_id": result.inserted_id},
            {"$set": {"event_id": payload["event_id"]}},
        )
        return payload

    @staticmethod
    async def list_events():
        docs = await EventService.collection.find().sort("timestamp", -1).to_list(length=100)
        for doc in docs:
            doc["event_id"] = str(doc.get("_id"))
        return docs
