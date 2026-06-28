import sqlite3

def initialize_db():
    # 1. Connect to the database file (it creates it if it doesn't exist)
    connection = sqlite3.connect("notes.db")
    
    # 2. Create a cursor object (this is what executes SQL commands)
    cursor = connection.cursor()
    
    # 3. Write our SQL command to create the table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    
    # 4. Commit (save) the changes and close the connection
    connection.commit()
    connection.close()

initialize_db()