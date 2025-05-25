import mysql.connector

DB_CONFIG = {
    'user': 'root',
    'password': 'x',
    'host': 'localhost',
    'database': 'ALX_prodev',    
}
TABLE_NAME = 'user_data'

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)
    
    offset = 0
    while True:
        cursor.execute(f"SELECT user_id, name, age FROM {TABLE_NAME} LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over age 25."""
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        filtered_batch = [user for user in batch if user['age'] > 25]  # Loop 2
        yield filtered_batch

if __name__ == "__main__":
    try:
        for users in batch_processing(100):  # Loop 3 (for output)
            for user in users:
                print(user)
    except Exception as e:
        print("Error occurred, stopping:", e)
