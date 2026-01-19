from fastapi import FastAPI

app = FastAPI(title="Production API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
