import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("workflowos.desktop_agent")


@dataclass
class DesktopEvent:
    source: str
    event_type: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    payload: dict[str, Any] = field(default_factory=dict)


class DesktopActivityAgent:
    def __init__(self):
        self.events: list[DesktopEvent] = []

    def observe(self, source: str, event_type: str, payload: dict[str, Any] | None = None) -> DesktopEvent:
        event = DesktopEvent(source=source, event_type=event_type, payload=payload or {})
        self.events.append(event)
        logger.info("Captured event: %s / %s", source, event_type)
        return event

    def summarize(self) -> dict[str, Any]:
        return {
            "event_count": len(self.events),
            "recent_events": [
                {
                    "source": event.source,
                    "event_type": event.event_type,
                    "timestamp": event.timestamp.isoformat(),
                    "payload": event.payload,
                }
                for event in self.events[-10:]
            ],
        }


if __name__ == "__main__":
    agent = DesktopActivityAgent()
    agent.observe("gmail", "email_opened", {"subject": "Customer request: 1045"})
    agent.observe("crm", "customer_record_opened", {"customer_id": "CUST-1045"})
    agent.observe("slack", "team_notification_sent", {"channel": "support-team"})
    print(agent.summarize())
