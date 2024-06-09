import streamlit as st 
import sqlite3 
from database2 import Database

class App:
    def __init__(self):
        self.db = Database()
        self.db.initialize_database()  
        # self.conn = self.db.connect()
        self.title = "Form to input Data"

    def get_employee_names(self):
        self.title = "Input employee Data"
        with st.form(key="employee_form"):
            employee_name = st.text_input("Employee Name")
            salary = st.number_input("Salary")
            phone_number = st.number_input("Phone Number")
            email = st.text_input("Email")
            submit_button = st.form_submit_button("Submit")
        if submit_button:
            sql = "INSERT INTO Employees (name, salary, phone_number, email) VALUES (?, ?, ?, ?) "
            data = (employee_name, salary, phone_number, email)
            self.db.execute(sql, data)
            st.success("Employee added successfully!")
            return employee_name
        
    def get_drug_details(self):
        self.title = "Input Drugs Data"
        with st.form(key="drug_form"):
            drug_name = st.text_input("Drug Name")
            drug_quantity = st.number_input("Drug Quantity")
            drug_price = st.number_input("Drug Price")
            stock_remaining = st.number_input("Stock Remaining")
            submit_button = st.form_submit_button("Submit")
        if submit_button:
            sql = "INSERT INTO Drugs_items (name, quantity_supplied, price, stock_remaining) VALUES (?, ?, ?, ?) "
            data = (drug_name, drug_quantity, drug_price, stock_remaining)
            self.db.execute(sql, data)
            st.success("Drug added successfully!")
            return drug_name
        
    def get_doctor(self):
        self.title = "Input Doctors details"
        with st.form(key="doctor_form"):
            doctor_name = st.text_input("Doctor Name")
            doctor_speciality = st.text_input("Doctor Speciality")
            phone_number = st.number_input("Phone Number")
            email = st.text_input("Email")
            region = st.text_input("Region")
            submit_button = st.form_submit_button("Submit")
        if submit_button:
            sql = "INSERT INTO Doctors_table (name, specialization, phone_number, email, region ) VALUES (?, ?, ?, ?, ?) "
            data = (doctor_name, doctor_speciality, phone_number, email, region)
            self.db.execute(sql, data)
            st.success("Doctor added successfully!")
            return doctor_name
        
    def run(self):
        st.title(self.title)
        st.sidebar.header("Select Form")
        form = st.sidebar.selectbox("Form", ("Employee", "Drug", "Doctor"))

        if form == "Employee":
            self.get_employee_names()
        elif form == "Drug":
            self.get_drug_details()
        elif form == "Doctor":
            self.get_doctor()

