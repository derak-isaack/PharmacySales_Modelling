import sqlite3
import streamlit as st
from database2 import Database 
from helpers import App
import mysql.connector
import socket
import json
from quixstreams import Application

#Configure streamlit with quixstreams
app = Application(
    broker_address= 'localhost:9092',
    loglevel= 'DEBUG'
)

db = Database(db_user='root', db_password='@admin#2024*10', db_host='localhost', db_name='pharmaflow')
db.initialize_database()  
conn = db.connect()

def get_employee_names():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Employees")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names

def get_drug_names():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Drugs_items")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names

def get_doctor_names():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Doctors_table")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names   

# def send_data(data):
#     """Sends individual data points from `data` to ncat server.

#     Args:
#         data (str): The data string containing comma-separated values.
#     """
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect(("localhost", 8000))  

#         # Split data into individual values 
#         data_points = data.split(",")
#         for value in data_points:
#             s.sendall(f"{value}\n".encode('utf-8'))
            
#         s.close()
        
#     except ConnectionError as e:
#         st.error(f"Error sending data to ncat server: {e}")

# def send_data_quixstreams(data):
#     app = Application(
#         broker_address="localhost:9092",
#         loglevel="DEBUG"
#     )
#     with app.get_producer() as producer:
#         producer.produce(
#             topic="pharmacy-sales-stream",
#             value=json.dumps(data)
#         )
        
        
def main():

    st.set_page_config(page_title='Sales Dashboard', page_icon=':bar_chart:', layout='wide')
    st.title('Pharmacy Sales User Input Form')

    with st.form(key='sales_form'):
    # Sales details
        emp_id = st.selectbox("Select Employee ID", get_employee_names()) 
        drug_id = st.selectbox("Select Drug ID", get_drug_names())  
        doc_id = st.selectbox("Select Doctor ID", get_doctor_names())  
        quantity_sold = st.number_input("Quantity Sold")
        date_sold = st.date_input("Date of Sale")
        pharmacy_name = st.text_input("Pharmacy Name")
        pharmacy_region = st.text_input("Pharmacy Region")
        submit_button = st.form_submit_button(label='Submit Sale')

    if submit_button:
        conn = db.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO Sales (emp_id, drug_id, doc_id, pharmacy_name, pharmacy_region, quantity_sold, date_sold) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (int(emp_id), int(drug_id), int(doc_id), pharmacy_name, pharmacy_region, float(quantity_sold), date_sold)
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
        st.success('Sale data submitted successfully!')
        
        data_dict = {
            "emp_id": emp_id,
            "drug_id": drug_id,
            "doc_id": doc_id,
            "pharmacy_name": pharmacy_name,
            "pharmacy_region": pharmacy_region,
            "quantity_sold": quantity_sold,
            "date_sold": str(date_sold)
        }
        data_json = json.dumps(data_dict)
        with app.get_producer() as producer:
            producer.produce(
                topic="pharmacy-sales-stream",
                value=json.dumps(data_json)
            )
        # send_data_quixstreams(data_json)
        st.success('Data sent to the server successfully!')


if __name__ == "__main__":
    main()
    app = App()
    app.run()
