import sqlite3
import easygui as e

# Connect to SQLite database.
conn = sqlite3.connect("movie database.db")
cursor = conn.cursor()



# Input add movie functionality.
choice = e.buttonbox("Choose any option:", "Movie database",
                    choices=["Add movie", "Delete movie", "View", "Edit", "Exit"])
    
if choice == "Add movie":
    field_names = ["Title", "Year(between 1900-2024)", "Rating ( e.g., PG, R)", "Duration(minutes, greater than 60)", ]
    while True:
        field_values = e.multenterbox("Enter movie details:", "Add movie", field_names)

        if field_values is None:
            break

        error = False
        for i in range(4):
            if field_values[i] == "":
                e.msgbox("fill all fields")
                error = True
                break

        if error:
            continue

        if int(field_values[1]) < 1900 or int(field_values[1]) > 2024:
            e.msgbox("Invalid movie year!", "Error")
            continue

        if int(field_values[3]) < 60:
            e.msgbox("Invalid movie duration!", "Error")
            continue

        cursor.execute("INSERT INTO Movie (title, Year, Rating, Duration) VALUES(?, ?, ?, ?)",
                    (field_values[0], int(field_values[1]), field_values[2], int(field_values[3])))
        conn.commit()
        e.msgbox("Movie added successfully!", "Success")
        break

if choice == "Delete movie":
    cursor.execute("SELECT title FROM Movie")
    movies = cursor.fetchall()
    if not movies:
        e.msgbox("No movies in the database!", "Error")
    else:
        movie_titles = [row[0] for row in movies]
        movie_delete = e.choicebox("Choose a movie to delete:", "Delete movie", movie_titles)
        if movie_delete is None:
            pass
        else:
            cursor.execute("DELETE FROM Movie WHERE title=?", (movie_delete,))
            conn.commit()
            e.msgbox("Movie deleted successfully!", "Success")

    
cursor = conn.cursor()
for row in cursor.execute("SELECT * FROM Movie"):
    print(row)

conn.commit()


    

