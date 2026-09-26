from app.db.mongo import mongo_db
from app.models.workflow import Workflow


class WorkflowService:
    collection = mongo_db["workflows"]

    @staticmethod
    async def create_workflow(workflow: Workflow):
        data = workflow.model_dump()
        result = await WorkflowService.collection.insert_one(data)
        workflow.workflow_id = str(result.inserted_id)
        await WorkflowService.collection.update_one(
            {"_id": result.inserted_id},
            {"$set": {"workflow_id": workflow.workflow_id}},
        )
        payload = workflow.model_dump()
        payload["workflow_id"] = workflow.workflow_id
        return payload

    @staticmethod
    async def list_workflows():
        docs = await WorkflowService.collection.find().sort("created_at", -1).to_list(length=100)
        result = []
        for doc in docs:
            doc["workflow_id"] = str(doc.get("_id"))
            result.append(doc)
        return result

    @staticmethod
    async def get_workflow(workflow_id: str):
        doc = await WorkflowService.collection.find_one({"workflow_id": workflow_id})
        if not doc:
            return None
        doc["workflow_id"] = str(doc.get("_id"))
        return doc
