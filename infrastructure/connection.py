import mysql.connector

USER = 'root'
PASSWORD = 'mypass1234'
HOST = 'localhost'
DATABASE = 'sistema_matriculas'

def get_connection():
    return mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)

def get_cursor():
    connection = get_connection()
    return connection.cursor()

