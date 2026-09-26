from collections import Counter

from app.db.mongo import mongo_db


class InsightService:
    collection = mongo_db["events"]

    @staticmethod
    async def generate_patterns():
        events = await InsightService.collection.find().sort("timestamp", -1).to_list(length=100)
        if not events:
            return [
                {
                    "name": "Customer Request Processing",
                    "confidence": 0.92,
                    "description": "Gmail -> Download attachment -> CRM update -> Slack notification",
                    "sources": ["gmail", "file_system", "crm", "slack"],
                    "status": "suggested",
                }
            ]

        source_order = [event.get("source") for event in events if event.get("source")]
        counts = Counter(source_order)

        if not counts:
            return []

        top_sources = [source for source, _ in counts.most_common(4)]
        pattern = {
            "name": "Customer Request Processing",
            "confidence": 0.92,
            "description": "A repeated pattern combining email intake, CRM lookup, document handling, and team notification.",
            "sources": top_sources,
            "status": "suggested",
        }

        return [pattern]
