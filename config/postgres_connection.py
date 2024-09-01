from psycopg2 import connect,OperationalError,sql
import sqlite3


def connect_database():
    try:
        conn =connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5432",
            )
        print("Connected to the database")
        return conn
    except OperationalError as e:
        print(f"Database connection error: {e}")
        return 








