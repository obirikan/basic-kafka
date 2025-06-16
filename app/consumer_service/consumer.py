from kafka import KafkaConsumer
import os
import json
from dotenv import load_dotenv
load_dotenv()

TOPIC='order_details'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=os.getenv("AIVEN_CLOUD"),
    security_protocol=os.getenv("SSL_PROTOCOL"),
    ssl_cafile=os.getenv("SSL_CAFILE"),
    ssl_certfile=os.getenv("SSL_CERTFILE"),
    ssl_keyfile=os.getenv("SSL_KEYFILE"),
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started...")
for message in consumer:
    print(f"Received: {message.value}")
