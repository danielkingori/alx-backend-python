import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Add a new column "email" to the users table
cursor.execute("ALTER TABLE users ADD COLUMN email TEXT")

conn.commit()
conn.close()
print("Column 'email' added to users table.")
