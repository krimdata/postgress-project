import psycopg2
import csv

DB_NAME = "my_database"
DB_USER = "admin"
DB_PASS = "password"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)
cursor = conn.cursor()

def import_csv(file_path, table_name, columns):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Ignorer l'en-tête
        for row in reader:
            try:
                cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({','.join(['%s']*len(row))})", row)
            except psycopg2.IntegrityError:
                conn.rollback()  # Ignorer
                conn.rollback()  # Ignorer les erreurs de doublons
            else:
                conn.commit()

# Importation des fichiers CSV
import_csv("../data/customers.csv", "customers", "name, email")
import_csv("../data/products.csv", "products", "name, price")
import_csv("../data/orders.csv", "orders", "customer_id, product_id, quantity")

print("Importation terminée avec succès.")

cursor.close()
conn.close()
