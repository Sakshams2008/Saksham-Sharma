import sqlite3
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