import sqlite3


def update_note(note_id, title, content):
    connection = sqlite3.connect("notes.db")
    cursor = connection.cursor()
    # Update the columns only for the matching unique ID
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, note_id))
    connection.commit()
    connection.close()

def delete_note(note_id):
    connection = sqlite3.connect("notes.db")
    cursor = connection.cursor()
    # Permanently delete the row matching the unique ID
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    connection.commit()
    connection.close()

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

def add_note(title, content):
    connection = sqlite3.connect("notes.db")
    cursor = connection.cursor()
    # Using '?' placeholders for security
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    connection.commit()
    connection.close()

def get_all_notes():
    connection = sqlite3.connect("notes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()  # This grabs our list of tuples
    connection.close()
    return notes


'''
--- TEMPORARY TEST CODE ---
if __name__ == "__main__":
    # 1. Make sure the table is initialized
    initialize_db()
    
    # 2. Add a test note
    print("Adding a test note...")
    add_note("Test Title", "This is a test note content!")
    
    # 3. Retrieve all notes and print them
    print("Retrieving all notes:")
    all_notes = get_all_notes()
    print(all_notes)
'''