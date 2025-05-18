import mysql.connector
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection details (Move to a config file or environment variables for production)
DB_CONFIG = {
    'user': 'myuser',  # Replace with your MySQL username
    'password': 'mypassword',  # Replace with your MySQL password
    'host': 'localhost',  # Or your MySQL host
    'database': 'ALX_prodev',
}
TABLE_NAME = 'user_data'


def stream_users():
    """
    Fetches rows one by one from the user_data table using a generator.
    Yields each row as a tuple.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for easier access

        query = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(query)

        # Use a single loop with yield
        for row in cursor:
            yield row  # Yield each row individually

        logging.info("Finished streaming users.")

    except mysql.connector.Error as err:
        logging.error(f"Error fetching data: {err}")
        yield None # yield None in case of error
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            logging.info("MySQL connection closed.")



if __name__ == "__main__":
    # Example usage:
    user_generator = stream_users()

    if user_generator is not None:
        for user in user_generator:
            if user is not None:
                print(user)  # Process each user row as needed
            else:
                print("Error occurred, stopping")
                break
