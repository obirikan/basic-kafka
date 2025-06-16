# 📦 Kafka FastAPI Demo

A minimal FastAPI-based microservice architecture using Kafka for event streaming and messaging between services.

---

## 📂 Project Structure

```
kafka_fastapi_demo/
├── app/
│   ├── endpoint_trigger.py       # FastAPI app (serves endpoints and triggers Kafka logic)
│   ├── consumer_service/
│   │   └── consumer.py           # Kafka consumer (listens to topic, handles events)
│   ├── producer_service/
│   │   └── producer.py           # Kafka producer (publishes messages to topic)
├── requirements.txt              # Python dependencies
└── docker-compose.yml            # Kafka & Zookeeper setup
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/kafka_fastapi_demo.git
cd kafka_fastapi_demo
```

### 2. Start Kafka and Zookeeper

```bash
docker-compose up -d
```

Make sure ports `9092` (Kafka) and `2181` (Zookeeper) are not in use.

### 3. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn app.endpoint_trigger:app --reload
```

App will be available at: `http://127.0.0.1:8000`

---

## 📬 API Endpoints

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| GET    | `/`           | Health check route                |
| POST   | `/send/{msg}` | Sends a message to Kafka producer |

---

## 🔪 Example Usage

```bash
curl -X POST http://127.0.0.1:8000/send/HelloKafka
```

Kafka Producer sends the message, and Kafka Consumer (if running) picks it up.

---

## 📦 Requirements

```text
fastapi
uvicorn
kafka-python==2.0.2
mypy-extensions==0.4.3
pathspec==0.9.0
platformdirs==2.4.0
tomli==1.2.2
typing-extensions==4.0.1
```


## ✅ To Do

* [ ] Add graceful consumer shutdown
* [ ] Add `.env` config support
* [ ] Add retry and error handling
* [ ] Write unit/integration tests

---

## 📜 License

MIT
