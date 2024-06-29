from quixstreams import Application
import json

def process_message(msg):
  data = json.loads(msg.value())
  if data is not None:  # Check if data is not None
    store_item = data["pharmacy_name"]
    total_quantity = data["total_quantity_sold"]
    print(f"Store-Item: {store_item}, Total Quantity Sold: {total_quantity}")
  else:
    print("Received None data")  # Handle missing data (optional)


def main():
  app = Application(
      broker_address="localhost:9092",
      loglevel="DEBUG",
      consumer_group="streamlit-tracker",
      auto_offset_reset="earliest"
  )

  with app.get_consumer() as consumer:
    consumer.subscribe(["streamlit-sales-tracker-output"])  # Adjust topic name if needed
    
    while True:
      msg = consumer.poll(10)  # Adjust polling interval as needed
      if msg is None:
        print("waiting...")
      elif msg.error() is not None:
        print(f"Consumer error: {msg.error()}")
      else:
        process_message(msg)

if __name__ == "__main__":
  main()
