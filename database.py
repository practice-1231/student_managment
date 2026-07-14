import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="student_db",
        user="postgres",
        password="YOUR_PASSWORD",
        port="5432"
    )
    return connection