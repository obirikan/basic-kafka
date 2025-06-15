# simple kafka setup
This is a basic Kafka producer-consumer project using FastAPI.
It lets you send and consume messages through HTTP.


| File                 | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| `main.py`            | Starts FastAPI server, triggers consumer in background     |
| `producer.py`        | Defines how to send messages to Kafka                      |
| `consumer.py`        | Defines how to read messages from Kafka                    |
| `docker-compose.yml` | Spins up Kafka & Zookeeper
| `requirements.txt`   | Lists Python packages (`fastapi`, `confluent-kafka`, etc.) |



kafka_fastapi_demo/
├── app/
│   ├── main.py         # 🚀 FastAPI app (starts Kafka consumer + API endpoints)
│   ├── producer.py     # 📨 Kafka producer logic (sends messages to topic)
│   └── consumer.py     # 📥 Kafka consumer logic (reads from topic)
├── requirements.txt    # 📦 Python dependencies
└── docker-compose.yml  # 🐳 Kafka + Zookeeper 

