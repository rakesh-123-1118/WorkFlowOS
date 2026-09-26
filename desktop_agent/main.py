from fastapi import FastAPI

app = FastAPI(title="WorkFlowOS Desktop Agent")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "workflowos-desktop-agent"}
