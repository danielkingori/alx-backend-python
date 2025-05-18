import mysql.connector
import uuid
import csv
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection details (Move to a config file or environment variables for production)
DB_CONFIG = {
    'user': 'root',  # Or your MySQL username
    'password': 'your_mysql_password',  # Or your MySQL password
    'host': 'localhost',  # Or your MySQL host
    # Note:  We don't include 'database' here initially, as we might create it.
}

CSV_FILE = 'user_data.csv'
DATABASE_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'


def connect_db():
    """
    Connects to the MySQL database server.

    Returns:
        mysql.connector.connection_cext.CMySQLConnection: A connection object on success, None on failure.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        logging.info("Successfully connected to the MySQL server.")
        return connection
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to MySQL server: {err}")
        return None  # Explicitly return None for error handling


def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist.

    Args:
        connection: A MySQL connection object.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
        logging.info(f"Database '{DATABASE_NAME}' created or already exists.")
    except mysql.connector.Error as err:
        logging.error(f"Error creating database '{DATABASE_NAME}': {err}")
        sys.exit(1)  # Exit on critical error
    finally:
        cursor.close()


def connect_to_prodev():
    """
    Connects to the ALX_prodev database in MySQL.  Assumes the database exists.

    Returns:
        mysql.connector.connection_cext.CMySQLConnection: A connection object on success, None on failure.
    """
    db_config_with_db = DB_CONFIG.copy()  # Create a copy to avoid modifying the original
    db_config_with_db['database'] = DATABASE_NAME
    try:
        connection = mysql.connector.connect(**db_config_with_db)
        logging.info(f"Successfully connected to the '{DATABASE_NAME}' database.")
        return connection
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to '{DATABASE_NAME}' database: {err}")
        return None


def create_table(connection):
    """
    Creates the table user_data if it does not exist with the required fields.

    Args:
        connection: A MySQL connection object.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10, 2) NOT NULL,
                INDEX (user_id)
            )
        """)  # Corrected syntax for index
        logging.info(f"Table '{TABLE_NAME}' created or already exists.")
        connection.commit()  # Commit the table creation
    except mysql.connector.Error as err:
        logging.error(f"Error creating table '{TABLE_NAME}': {err}")
        sys.exit(1)  # Exit on critical error
    finally:
        cursor.close()


def insert_data(connection, data):
    """
    Inserts data into the database if it does not exist.  Handles potential duplicates.

    Args:
        connection: A MySQL connection object.
        data: A list of tuples, where each tuple represents a row of data.
    """
    cursor = connection.cursor()
    insert_query = f"""
        INSERT INTO {TABLE_NAME} (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.executemany(insert_query, data)  # Use executemany for efficiency
        connection.commit()
        logging.info(f"{cursor.rowcount} rows inserted into '{TABLE_NAME}'.")
    except mysql.connector.Error as err:
        logging.error(f"Error inserting data into '{TABLE_NAME}': {err}")
        connection.rollback() # Rollback on error.
        sys.exit(1)
    finally:
        cursor.close()



def load_csv_data(filename):