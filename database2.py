import sqlite3

class Database:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name

    def initialize_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        with open('pharmacy_sales_tracker.sql', 'r') as file:
            sql_script = file.read()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def execute(self, sql, data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
