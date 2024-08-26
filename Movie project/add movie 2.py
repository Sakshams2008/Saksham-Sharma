import sqlite3
import easygui as e

# Connect to SQLite database.
conn = sqlite3.connect("movie database.db")
cursor = conn.cursor()


while True:
# Input add movie functionality.
    choice = e.buttonbox("Choose any option:", "Movie database",
                        choices=["Add movie", "Delete movie", "View existing movie", "Edit movie", "Exit"])
        
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
            add_another = e.ynbox("Would you like to add another movie?", "Add another movie")
            if add_another:
                continue
            else:
                break
            

    if choice == "Delete movie":
        while True:
            cursor.execute("SELECT title FROM Movie")
            movies = cursor.fetchall()
            if not movies:
                e.msgbox("No movies in the database!", "Error")
                break
            else:
                movie_titles = [row[0] for row in movies]
                movie_delete = e.choicebox("Choose a movie to delete:", "Delete movie", movie_titles)
                if movie_delete is None:
                    break
                else:
                    cursor.execute("DELETE FROM Movie WHERE title=?", (movie_delete,))
                    conn.commit()
                    e.msgbox("Movie deleted successfully!", "Success")
                    delete_another = e.ynbox("Do you want to delete another movie?", "Delete another movie")
                    if not delete_another:
                        break

    if choice == "View existing movie":
        while True:
            cursor.execute("SELECT title FROM Movie")
            movies = cursor.fetchall()
            if not movies:
                e.msgbox("No movies in the database!", "Error")
                break
            else:
                movie_titles = [row[0] for row in movies]
                movie_select = e.choicebox("Choose a movie to view:", "View movie", movie_titles)
                if movie_select is None:
                    break
                else:
                    cursor.execute("SELECT * FROM Movie WHERE title=?", (movie_select,))
                    movie_details = cursor.fetchone()
                    output = "Title: {}\nYear: {}\nRating: {}\nDuration: {}".format(movie_details[1], movie_details[2], movie_details[3], movie_details[4])
                    e.msgbox(output, "Movie Details")
            view_another = e.ynbox("Do you want to view another?", "View another")
            if not view_another:
                break

    if choice == "Edit movie":
        while True:
            cursor.execute("SELECT title FROM Movie")
            movies = cursor.fetchall()
            if not movies:
                e.msgbox("No movies in the database!", "Error")
                break
            else:
                movie_titles = [row[0] for row in movies]
                movie_edit = e.choicebox("Choose a movie to edit:", "Edit movie", movie_titles)
                if movie_edit is None:
                    break
                else:
                    cursor.execute("SELECT * FROM Movie WHERE title=?", (movie_edit,))
                    movie_details = cursor.fetchone()
                    field_names = ["Title", "Year(between 1900-2024)", "Rating ( e.g., PG, R)", "Duration(minutes, greater than 60)"]
                    field_values =[ movie_details[1], str(movie_details[2]), movie_details[3], str(movie_details[4])]
                    new_values = e.multenterbox("Edit movie details:", "Edit movie", field_names, field_values)
                    
                    if new_values is None:
                        break

                    error = False
                    for i in range(4):
                        if new_values[i] == "":
                            e.msgbox("Fill all fields")
                            error = True
                            break

                    if error:
                        continue

                    if int(new_values[1]) < 1900 or int(new_values[1]) > 2024:
                        e.msgbox("Invalid movie year!", "Error")
                        continue

                    if int(new_values[3]) < 60:
                        e.msgbox("Invalid movie duration!", "Error")
                        continue

                    cursor.execute("UPDATE Movie SET title=?, Year=?, Rating=?, Duration=? WHERE title=?",
                                (new_values[0], int(new_values[1]), new_values[2], int(new_values[3]), movie_edit))
                    conn.commit()
                    e.msgbox("Movie edited successfully!", "Success")
                    edit_another = e.ynbox("Do you want to edit another movie?", "Edit another movie")
                    if not edit_another:
                        break
        
    if choice == "Exit":
        break
                

    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM Movie"):
        print(row)

    conn.commit()


    

