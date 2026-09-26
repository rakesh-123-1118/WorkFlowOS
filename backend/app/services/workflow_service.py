from app.db.mongo import mongo_db
from app.models.workflow import Workflow


class WorkflowService:
    collection = mongo_db["workflows"]

    @staticmethod
    async def create_workflow(workflow: Workflow):
        result = await WorkflowService.collection.insert_one(workflow.model_dump())
        workflow.workflow_id = str(result.inserted_id)
        await WorkflowService.collection.update_one(
            {"_id": result.inserted_id},
            {"$set": {"workflow_id": workflow.workflow_id}},
        )
        return workflow.model_dump()

    @staticmethod
    async def list_workflows():
        docs = await WorkflowService.collection.find().to_list(length=100)
        return [{**doc, "workflow_id": str(doc.get("_id"))} for doc in docs]

    @staticmethod
    async def get_workflow(workflow_id: str):
        doc = await WorkflowService.collection.find_one({"workflow_id": workflow_id})
        if not doc:
            return None
        doc["workflow_id"] = str(doc.get("_id"))
        return doc
