from kafka import KafkaProducer
from kafka.errors import KafkaError
import os
import json
from dotenv import load_dotenv

load_dotenv()


print("aiven---producer ", os.getenv("AIVEN_CLOUD"))

producer = KafkaProducer(
    bootstrap_servers=os.getenv("AIVEN_CLOUD"),
    security_protocol=os.getenv("SSL_PROTOCOL"),
    ssl_cafile=os.getenv("SSL_CAFILE"),
    ssl_certfile=os.getenv("SSL_CERTFILE"),
    ssl_keyfile=os.getenv("SSL_KEYFILE"),
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

def send_message(topic, message):
    try:
        future = producer.send(topic, value={"message": message})
        record_metadata = future.get(timeout=10)
        print(f"Sent to {record_metadata.topic}[{record_metadata.partition}]")
    except KafkaError as e:
        print(f"Kafka error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")