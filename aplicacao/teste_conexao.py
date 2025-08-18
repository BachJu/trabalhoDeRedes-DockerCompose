import mysql.connector
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

print("USER:", os.getenv("MYSQL_USER"))
print("PASS:", os.getenv("MYSQL_PASSWORD"))
print("DB:", os.getenv("MYSQL_DATABASE"))
print("HOST:", os.getenv("MYSQL_HOST"))
print("PORT:", os.getenv("MYSQL_PORT"))

try:
    con = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD") or None,
        database=os.getenv("MYSQL_DATABASE"),
        port=os.getenv("MYSQL_PORT", 3306)
    )
    print("Conexão bem-sucedida!")
    con.close()
except mysql.connector.Error as e:
    print("Erro ao conectar:", e)