import psycopg2
from dotenv import load_dotenv
import os

def get_connection():
    print("Cargando variables")
    load_dotenv()
    conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )
    print("Conexion realizada con exito")
    return conn


