import mysql.connector

# Generator: stream user ages one at a time
def stream_user_ages():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='x',
        database='ALX_prodev'
    )
    cursor = connection.cursor()

    query = "SELECT age FROM user_data"
    cursor.execute(query)

    for (age,) in cursor:
        yield age

    cursor.close()
    connection.close()

# Use generator to compute average age
def compute_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():  # First loop
        total_age += age
        count += 1

    average_age = total_age / count if count else 0
    print(f"Average age of users: {average_age:.2f}")

if __name__ == '__main__':
# Run the script
    compute_average_age()
