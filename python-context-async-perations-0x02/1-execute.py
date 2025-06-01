import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params else ()
        self.connection = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print("Database connection opened.")
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_name = "ALX_prodev.db"
    
    # Setup: Create a users table and insert data
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cur.execute("DELETE FROM users")  # Clear old data
        cur.execute("ALTER TABLE users ADD COLUMN age INTEGER")
        cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
            ('Alice', 22), ('Bob', 30), ('Charlie', 28), ('Diana', 24)
        ])
        conn.commit()
    
    # Use ExecuteQuery context manager to run a parameterized query
    query = "SELECT * FROM users WHERE age > ?"
    param = (25,)
    
    with ExecuteQuery(db_name, query, param) as results:
        print("Query Results (age > 25):")
        for row in results:
            print(row)
