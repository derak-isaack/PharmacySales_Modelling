from quixstreams import Application
import json 

app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
    consumer_group="streamlit-reader",
    #Instructions to begin on the latest data
    auto_offset_reset="latest"
)

def process_message(msg):
    data = json.loads(msg.value())
    print(f"Received data: {data}")

def main():
    with app.get_consumer() as consumer:
        consumer.subscribe(["streamlit-sales-tracker"])
        
        while True:
            #Poll represents how many seconds the kafka should wait for the topics
            msg = consumer.poll(10)  
            
            if msg is None:
                print("waiting...")
            elif msg.error() is not None:
                print(f"Consumer error: {msg.error()}")
            else:
                process_message(msg)

if __name__ == "__main__":
    main()
            
        
        
    