from fastapi import FastAPI

app = FastAPI(title="My CI/CD App", version="1.0.0")

@app.get("/")
def home():
    return {
        "message": "Hello from CI/CD!",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "name": f"Item number {item_id}"
    }