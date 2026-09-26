from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.models.workflow import Workflow
from app.services.workflow_service import WorkflowService

router = APIRouter(tags=["workflows"])


class WorkflowCreateRequest(BaseModel):
    name: str
    description: str
    intent: str


@router.get("/workflows")
async def list_workflows():
    return await WorkflowService.list_workflows()


@router.post("/workflows", status_code=201)
async def create_workflow(payload: WorkflowCreateRequest):
    if not payload.name or not payload.intent:
        raise HTTPException(status_code=400, detail="name and intent are required")

    workflow = Workflow(
        name=payload.name,
        description=payload.description,
        intent=payload.intent,
        triggers=[{"type": "email", "source": "gmail"}],
        steps=[],
    )

    created = await WorkflowService.create_workflow(workflow)
    return created


@router.get("/workflows/{workflow_id}")
async def get_workflow(workflow_id: str):
    workflow = await WorkflowService.get_workflow(workflow_id)
    if not workflow:
        raise HTTPException(status_code=404, detail="workflow not found")
    return workflow
