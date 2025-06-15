from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Delivery failed:', err)
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_message(topic: str, message: str):
    p.produce(topic, message.encode('utf-8'), callback=delivery_report)
    p.flush()
