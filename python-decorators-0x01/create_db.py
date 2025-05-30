import sqlite3

#connecty to the sqlite db and create a file if doesn't exist
conn = sqlite3.connect('my_database.db')
#create a cursor object to execute sql commands

cursor = conn.cursor()

#create the users table

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

#insert into the table some datasets
cursor.execute("INSERT INTO users(name, age) VALUES(?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 20))

conn.commit()
conn.close()

print("database and users table created successifully")
