import sqlite3
import streamlit as st
from database2 import Database 
from helpers import App

db = Database()
db.initialize_database()  
conn = db.connect()

def get_employee_names():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Employees")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names

def get_drug_names():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Drugs_items")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names

def get_doctor_names():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Doctors_table")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names   

def main():

    st.set_page_config(page_title='Sales Dashboard', page_icon=':bar_chart:', layout='wide')
    st.title('Pharmacy Sales User Input Form')

    with st.form(key='sales_form'):
    # Sales details
        employee_name = st.selectbox("Select Employee", get_employee_names()) 
        drug_name = st.selectbox("Select Drug", get_drug_names())  
        doctor_name = st.selectbox("Select Doctor", get_doctor_names())  
        quantity_sold = st.number_input("Quantity Sold")
        date_sold = st.date_input("Date of Sale")
        pharmacy_name = st.text_input("Pharmacy Name")
        pharmacy_region = st.text_input("Pharmacy Region")
        submit_button = st.form_submit_button(label='Submit Sale')

    if submit_button:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = "INSERT INTO Sales (emp_id, drug_id, doc_id, pharmacy_name, pharmacy_region, quantity_sold, date_sold) VALUES (?, ?, ?, ?, ?, ?, ?)"
        data = (employee_name, drug_name, doctor_name, pharmacy_name, pharmacy_region, quantity_sold, date_sold)
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
        st.success('Sale data submitted successfully!')


if __name__ == "__main__":
    main()
    app = App()
    app.run()
