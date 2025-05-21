import csv
import uuid
import mysql.connector
from mysql.connector import errorcode

#connecting to DB
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='xxxx'
    )
    
#create database if doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database 'ALX_prodev' checked/created")
    finally:
        cursor.close()
#connects to the db
def connect_to_prodev():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='xxxx',
        database='ALX_prodev'
    )
#creates table
def create_table(connection):
    cursor = connection.cursor()
    create_stmt = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    );
    """
    cursor.execute(create_stmt)
    print("Table 'user_data' checked/created.")
    cursor.close()
#insert multiple rows
def insert_data(connection, data):
    cursor = connection.cursor()
    insert_stmt = """
    INSERT INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), age=VALUES(age)
    """
    cursor.executemany(insert_stmt, data)
    connection.commit()
    print(f"{cursor.rowcount} rows inserted")
    cursor.close()

#load the csv
def load_CSV(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield(str(uuid.uuid4()), row['name'], row['email'], float(row['age']))

#generator to stream data from the csv
def stream_user_data(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()

#main function to run all
def main():
    conn = connect_db()
    create_database(conn)
    conn.close()
    
    prodev_conn = connect_to_prodev()
    create_table(prodev_conn)
    
    data_gen = load_CSV("user_data.csv")
    insert_data(prodev_conn, list(data_gen))
    
    print("Streaming data")
    for row in stream_user_data(prodev_conn):
        print(row)
    prodev_conn.close()
    
#main run
if __name__ == "__main__":
    main()