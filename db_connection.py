import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Root@12345",
        database="ehs"
    )
    return connection
