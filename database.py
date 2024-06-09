import streamlit as st 
import sqlite3 

st.set_page_config(page_title="Home", page_icon=":tada:", layout="wide")
def get_connection():
    conn = sqlite3.connect('hospi_sales.db')
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            date DATE NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
def insert_data(date, name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sales (date, name, email)
        VALUES (?, ?, ?)
    ''', (date, name, email))
    conn.commit()
    conn.close()

create_table()
st.title("Welcome to the Rangers Hospital")

with st.form("my_form"):
    st.write("Please fill out the following sales details:")
    date = st.date_input("Date")
    name = st.text_input("Name")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        insert_data(date, name, email)
        st.success("Data saved successfully!")