import sqlite3
import easygui as e

# Connect to SQLite database.
conn = sqlite3.connect("movie database.db")
cursor = conn.cursor()



# Input add movie functionality.
def add_movie():
    title = e.enterbox("Enter the movie title:", "Add movie")
    if not title:
        e.msgbox("Title required!", "Error")
        return
    
    year = e.enterbox("Enter the movie year:", "Add movie")
    if not year or not year.isdigit():
        e.msgbox("Valid year required!", "Error")
        return
    
    rating = e.enterbox("Enter the movie rating (e.g., PG, R):", "Add movie")
    if not rating:
        e.msgbox("Rating is required!", "Error")
        return
    
    duration = e.enterbox("Enter the movie duration in minutes:", "Add movie")
    if not duration or not duration.isdigit():
        e.msgbox("Valid duration required!", "Error")
        return
    
    
    cursor.execute("INSERT INTO Movie (title, Year, Rating, Duration) VALUES(?, ?, ?, ?)",
                    (title, int(year), rating, int(duration)))
    conn.commit()
    e.msgbox("Movie added successfully!", "Success")

add_movie()
cursor = conn.cursor()
for row in cursor.execute("SELECT * FROM Movie"):
    print(row)

conn.commit()
