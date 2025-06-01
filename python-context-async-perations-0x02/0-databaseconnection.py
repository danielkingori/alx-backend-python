import sqlite3
class DatabaseConnections:
    def __init__(self, ALX_prodev):
        self.db_name = ALX_prodev
        self.connection = None
        self.cursor = None
        
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print("Database connection opened")
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    with DatabaseConnections("ALX_prodev.db") as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie')")
    
    # Use context manager to query the users
    with DatabaseConnections("example.db") as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print("Query Results:")
        for row in results:
            print(row)