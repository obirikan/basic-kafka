from fastapi import FastAPI
from app.producer_service.producer import send_message
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Kafka working!"}

@app.post("/send/{msg}")
async def send(msg: str):
    send_message("order_details", msg)
    return {"status": "sent", "message": msg}

if __name__ == "__endpoint_trigger__":
    uvicorn.run(app, host="0.0.0.0", port=8000)