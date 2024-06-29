from quixstreams import Application
from quixstreams.dataframe.dataframe import StreamingDataFrame
from quixstreams.state.types import State
import json, logging
import pandas as pd 


def process_message(msg):
    data = json.loads(msg.value())
    logging.info(f"Received data: {data}")
    # sdf.add_data(data)

def main():
    app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
    consumer_group="streamlit-reader",
    auto_offset_reset="earliest"
)
    
    input_topic = app.topic('streamlit-sales-tracker', value_deserializer='json')
    output_topic = app.topic('streamlit-sales-tracker-output', value_deserializer='json')
    
    def calculate_total_quantity(d: dict, state: State):
        if isinstance(d, str):
            d = json.loads(d)
        current_total = state.get("quantity_total", 0.0)
        new_total = current_total + float(d["quantity_sold"])
        state.set("quantity_total", new_total)
        d["total_quantity_sold"] = new_total
        logging.debug(f"Returning: {d}")
        return d

    def groupby_store_and_item(message):
        if isinstance(message, str):
            message = json.loads(message)
        return f"{message['drug_id']}--{message['pharmacy_name']}"
    

    
    sdf = app.dataframe(input_topic)
    sdf = sdf.group_by(key=groupby_store_and_item, name="pharmacy_item").apply(calculate_total_quantity, stateful=True)
    sdf = sdf.to_topic(output_topic)
    logging.debug("Starting...")
    app.run(sdf)
    
    
    
    with app.get_consumer() as consumer:
        consumer.subscribe(["streamlit-sales-tracker-output"])
        
        while True:
            msg = consumer.poll(1)
            if msg is None:
                print("waiting...")
            elif msg.error() is not None:
                print(f"Consumer error: {msg.error()}")
            else:
                process_message(msg)
                
                

if __name__ == "__main__":
    main()
