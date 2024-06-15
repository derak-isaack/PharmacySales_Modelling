import mysql.connector

class Database:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.initialize_database()
        
    def initialize_database(self):
        conn = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database = self.db_name  
        )
        cursor = conn.cursor()
        with open('pharmacy_sales_tracker.sql', 'r') as file:
            sql_script = file.read()
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        conn.close()
        # self.initialize_database_tables()

    # def initialize_database(self):
    #     conn = mysql.connector.connect(
    #         host=self.db_host,
    #         user=self.db_user,
    #         password=self.db_password,
    #         database=self.db_name
    #     )
    #     cursor = conn.cursor()
    #     with open('pharmacy_sales_tracker.sql', 'r') as file:
    #         sql_script = file.read()
    #     for statement in sql_script.split(';'):
    #         if statement.strip():
    #             cursor.execute(statement)
    #     conn.commit()
    #     conn.close()

    def connect(self):
        return mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name
        )

    def execute(self, sql, data):
        conn = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name
        )
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
        
host = 'localhost'
user = 'root'
password = '@admin#2024*10'
database = 'pharmaflow'
