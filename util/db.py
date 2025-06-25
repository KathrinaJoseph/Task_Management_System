# db.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",     # CHANGE THIS
        password="mysql", # CHANGE THIS
        database="market_system"
    )
