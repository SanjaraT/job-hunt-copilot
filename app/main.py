from fastapi import FastAPI
app = FastAPI(title = "AI Job Hunt Copilot")

@app.get("/health")
def health():
    return{"status" : "ok"}



