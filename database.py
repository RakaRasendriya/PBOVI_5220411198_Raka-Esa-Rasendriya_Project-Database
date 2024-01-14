import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='5220411198',
            user='root',
            password=''
        )
        print("Koneksi ke database berhasil")
    except Error as e:
        print(f"Error: {e}")

    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query berhasil dijalankan")
    except Error as e:
        print(f"Error: {e}")

def create_users_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255) NOT NULL,
        umur INT NOT NULL,
        jenis_kelamin VARCHAR(1) NOT NULL
    )
    """
    execute_query(connection, query)

def create_table_laki(connection):
    query = """
    CREATE TABLE IF NOT EXISTS laki (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        top VARCHAR(255),
        bottom VARCHAR(255),
        alas_kaki VARCHAR(255),
        tipe_pakaian VARCHAR(10)
    )
    """
    execute_query(connection, query)

def create_table_perempuan(connection):
    query = """
    CREATE TABLE IF NOT EXISTS perempuan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        inner_clothes VARCHAR(255),
        outer_clothes VARCHAR(255),
        bottom VARCHAR(255),
        alas_kaki VARCHAR(255),
        tipe_pakaian VARCHAR(10)
    )
    """
    execute_query(connection, query)

def create_table_tampilan(connection):
    query = """
    CREATE TABLE IF NOT EXISTS tampilan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        aksesoris VARCHAR(255),
        makeup VARCHAR(255)
    )
    """
    execute_query(connection, query)

create_connection()
connection = create_connection()
if connection.is_connected():
    create_users_table(connection)
    create_table_laki(connection)
    create_table_perempuan(connection)
    create_table_tampilan(connection)

    connection.close()
    print("Tabel berhasil dibuat")
