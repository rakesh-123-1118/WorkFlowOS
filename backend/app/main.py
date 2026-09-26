from fastapi import FastAPI
from app.api.routes import workflows

app = FastAPI(
    title="WorkFlowOS",
    description="AI-powered workflow automation orchestration backend",
    version="0.1.0",
)

app.include_router(workflows.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "workflowos-backend"}
