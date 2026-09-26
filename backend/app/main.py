from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import workflows, events, insights

app = FastAPI(
    title="WorkFlowOS",
    description="AI-powered workflow automation orchestration backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workflows.router, prefix="/api/v1")
app.include_router(events.router, prefix="/api/v1")
app.include_router(insights.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "workflowos-backend"}
