from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Project Aetheris — Security & Visibility Engine",
    version="0.1.0",
    description="AI-powered kernel visibility & security shield backend engine."
)

class KernelEvent(BaseModel):
    pid: int
    process_name: str
    syscall: str
    timestamp: Optional[datetime] = None
    severity: str = "INFO"

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "system": "Project Aetheris Engine",
        "status": "online",
        "shield_active": True
    }

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy", "service": "fastapi-engine"}

@app.post("/api/v1/telemetry", status_code=status.HTTP_201_CREATED)
def ingest_kernel_event(event: KernelEvent):
    return {
        "status": "received",
        "event_process": event.process_name,
        "syscall": event.syscall
    }
