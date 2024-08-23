import sqlite3
import easygui as e

# Connect to SQLite database.
conn = sqlite3.connect("movie database.db")
cursor = conn.cursor()



# Input add movie functionality.
choice = e.buttonbox("Choose any option:", "Movie database",
                        choices=["Add movie", "Delete movie", "View", "Edit", "Exit"])
    
if choice == "Add movie":
    field_names = ["Title", "Year", "Rating ( e.g., PG, R)", "Duration(minutes)", ]
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

        cursor.execute("INSERT INTO Movie (title, Year, Rating, Duration) VALUES(?, ?, ?, ?)",
                    (field_values[0], int(field_values[1]), field_values[2], int(field_values[3])))
        conn.commit()
        e.msgbox("Movie added successfully!", "Success")
        break
    

cursor = conn.cursor()
for row in cursor.execute("SELECT * FROM Movie"):
    print(row)

conn.commit()


    

