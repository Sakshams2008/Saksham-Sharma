import sqlite3
import easygui as e

# Connect to SQLite database.
conn = sqlite3.connect("movie database.db")
cursor = conn.cursor()

# Create the movie table
cursor.execute('''
    CREATE TABLE Movie (
        ID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Year DATE NOT NULL,
        Rating TEXT NOT NULL,
        Duration INTEGER NOT NULL
    )
''')
conn.commit()

# Input add movie functionality.
def add_movie():
    title = e.enterbox("Enter the movie title:", "Add movie")
    if not title:
        e.msgbox("Title required!", "Error")
        return