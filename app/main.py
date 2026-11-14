from fastapi import FastAPI
from app.db import init_schema
from app.auth.routes import router as auth_router


app = FastAPI(title = "AI Job Hunt Copilot")

@app.on_event("startup")
def on_startup():
    init_schema()

@app.get("/health")
def health():
    return{"status" : "ok"}

app.include_router(auth_router)

