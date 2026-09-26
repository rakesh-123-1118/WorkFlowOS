from fastapi import APIRouter

from app.services.insight_service import InsightService

router = APIRouter(tags=["insights"])


@router.get("/insights/patterns")
async def list_patterns():
    return await InsightService.generate_patterns()
