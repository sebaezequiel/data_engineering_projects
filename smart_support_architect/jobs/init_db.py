from db_connection import get_connection
import os

conn = get_connection()

base_path = os.path.dirname(__file__)
db_path = os.path.join(base_path, "..", "db")

db_files = os.listdir(db_path)

sorted_files = sorted(db_files)
filtered_files = [f for f in sorted_files if f.endswith(".sql")]

cursor = conn.cursor()
for i in filtered_files:
    with open(os.path.join(db_path, i), "r") as f:
        contenido = f.read()
    print(f"Executing {i}")
    cursor.execute(contenido)
    print(f"{i} execution successful")
    conn.commit()

conn.close()
print("Connection closed")