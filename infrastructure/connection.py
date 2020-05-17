import mysql.connector

connection_cred = {
    'user': 'root',
    'password': 'mypass1234',
    'host': 'localhost',
    'database': 'sistema_matriculas'
}

def get_connection():
    return mysql.connector.connect(**connection_cred)

def get_cursor():
    connection = get_connection()
    return connection.cursor()

