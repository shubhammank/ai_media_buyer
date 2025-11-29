from fastapi import FastAPI
from src.workflows.orchestrator import run_workflow

app=FastAPI()

@app.get("/")
def root():
    return {"status":"running"}

@app.post("/run")
def execute(payload: dict):
    return run_workflow(payload.get("query","test query"))
