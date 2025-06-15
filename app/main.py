import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from producer import send_message
from consumer import start_consumer

from fastapi import FastAPI

import threading

app = FastAPI()

threading.Thread(target=start_consumer, args=("test-topic",), daemon=True).start()

@app.get("/")
def root():
    return {"message": "Kafka go is working!"}

@app.post("/send/{msg}")
def send(msg: str):
    send_message("test-topic", msg)
    return {"status": "sent", "message": msg}


