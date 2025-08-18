import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Conexao:

    def __init__(self):
        self.con = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD') or None,
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT', 3306)
        )

    def __enter__(self):
        return self.con
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()