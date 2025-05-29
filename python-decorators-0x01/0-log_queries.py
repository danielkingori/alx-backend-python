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

@log_queries()
def run_query(query, params=None):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)")
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Example call
run_query("SELECT * FROM user")


            