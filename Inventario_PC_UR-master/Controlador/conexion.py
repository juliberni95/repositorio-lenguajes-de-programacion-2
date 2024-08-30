import mysql.connector

class DataBase:
    def __init__(self):
        self.connection= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='prueba_inv'
        )
        self.cursor=self.connection.cursor(buffered=True)