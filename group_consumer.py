from quixstreams import Application
import json

app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
    consumer_group="streamlit-tracker",
    auto_offset_reset="earliest"
)

def process_message(msg):
    data = json.loads(msg.value())
    print(f"Received data: {data}")
    # sdf.add_data()
    
def main():
    with app.get_consumer() as consumer:
        consumer.subscribe(["streamlit-sales-tracker-output"])
        
        while True:
            msg = consumer.poll(10)
            if msg is None:
                print("waiting...")
            elif msg.error() is not None:
                print(f"Consumer error: {msg.error()}")
            else:
                process_message(msg)
                
if __name__ == "__main__":
    main()