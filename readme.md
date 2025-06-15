# Simple Kafka Setup

This is a basic Kafka producer-consumer project using FastAPI.
It lets you send and consume messages through HTTP.

## Project Structure

| File                 | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| `main.py`            | Starts FastAPI server, triggers consumer in background     |
| `producer.py`        | Defines how to send messages to Kafka                      |
| `consumer.py`        | Defines how to read messages from Kafka                    |
| `docker-compose.yml` | Spins up Kafka & Zookeeper                                 |
| `requirements.txt`   | Lists Python packages (`fastapi`, `confluent-kafka`, etc.) |

```
kafka_fastapi_demo/
├── app/
│   ├── main.py         # 🚀 FastAPI app (starts Kafka consumer + API endpoints)
│   ├── producer.py     # 📨 Kafka producer logic (sends messages to topic)
│   └── consumer.py     # 📥 Kafka consumer logic (reads from topic)
├── requirements.txt    # 📦 Python dependencies
└── docker-compose.yml  # 🐚 Kafka + Zookeeper
```

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start Kafka and Zookeeper:

```bash
docker-compose up -d
```

3. Start FastAPI app:

```bash
uvicorn app.main:app --reload
```

4. Test sending a message:

```bash
curl -X POST http://localhost:8000/send/hello
```

