from confluent_kafka import Consumer, KafkaException

def start_consumer(topic: str):
    print(f"📥 Consuming from topic: {topic}")

    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe([topic])

    try:
        while True:
            print("⏳ Waiting for message...")  
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())

            print(f"📩 Received: {msg}")


    except KeyboardInterrupt:
        print("❌ Consumer interrupted")
    finally:
        c.close()
