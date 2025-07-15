import mysql.connector
from dotenv import load_dotenv
import os 

load_dotenv()

# se abre la conexion a la bd y se llaman a las variables de entorno
def get_connection():
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        database = os.getenv("DB_NAME")
    )

# print("Conexion OK")
# cursor = conn.cursor()
