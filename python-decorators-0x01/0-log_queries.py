import sqlite3
from functools import wraps

def log_queries():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log SQL statements if passed in kwargs or args
            print(f"[LOG] Executing function: {func.__name__}")
            if 'query' in kwargs:
                print(f"[SQL] Query: {kwargs['query']}")
            elif args:
                for arg in args:
                    if isinstance(arg, str) and arg.strip().lower().startswith(("select", "insert", "update", "delete")):
                        print(f"[SQL] Query: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")


            