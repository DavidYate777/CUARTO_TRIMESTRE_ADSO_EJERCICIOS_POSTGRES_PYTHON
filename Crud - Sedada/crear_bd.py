import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:

    conexion = psycopg2.connect(
        host=os.getenv("HOST"),
        database="postgres",  # Base por defecto
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        port=os.getenv("PORT")
    )

    conexion.autocommit = True

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE DATABASE sedada
    """)

    print("Base de datos creada correctamente")

    cursor.close()
    conexion.close()

except Exception as e:

    print("Error:", e)