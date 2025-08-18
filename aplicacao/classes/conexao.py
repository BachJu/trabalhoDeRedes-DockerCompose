import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Conexao:

    def __init__(self):
        self.con = mysql.connector.connect(
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )

    def __enter__(self):
        return self.con
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()