import psycopg2

DB_NAME = "my_database"
DB_USER = "admin"
DB_PASS = "password"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)
cursor = conn.cursor()

# Lire le fichier SQL
with open("../db/queries.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

queries = [q.strip() for q in sql_script.split(";") if q.strip()]

for query in queries:
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query:", query)
        print("Result:", result)
    except Exception as e:
        print("Error executing query:", query)
        print(e)

conn.commit()
cursor.close()
conn.close()
