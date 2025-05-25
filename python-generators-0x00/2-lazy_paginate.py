import mysql.connector

# Helper function to fetch a page of users
def paginate_users(page_size, offset):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='x',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return results

# Generator function to lazily paginate users
def lazy_paginate(page_size):
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        yield users
        offset += page_size
        
if __name__ =='__main__':
    for page in lazy_paginate(10):
        for user in page:
            print(user['user_id'], user['name'])  # adjust field names as per your table
