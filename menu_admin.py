from tkinter import Entry, Misc, messagebox, ttk
from tkinter.constants import END

import function


def admin_menu():
    window_admin = function.toplevel_window("MOVIETIME Admin", "950x600")
    window_admin.grab_set()
    panel_calog_movie_admin = function.panel_window(window_admin, 900, 231, 20, 20)
    catalog_movie_admin = function.catalog_view(panel_calog_movie_admin, ["Movie", "Genres", "Director", "Rating"], [200, 242, 200, 250])   # panel that shows the existent movies/series
    with open("database/movies.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
        for line in f:
            words = line.split(";")
            catalog_movie_admin.insert("", "end", values=(
                words[0], words[1], words[2], words[3]))        # inserts the whole data in movies.csv by lines

    panel_option_admin = function.panel_window(window_admin, 900, 200, 20, 300)

    #group of labels and entries
    lbl_movie_name = function.place_label(panel_option_admin, "Movie Name: ", 20, 20)
    movie_name = function.place_entry(panel_option_admin, 20, 20, 40)

    lbl_movie_genre = function.place_label(panel_option_admin, "Genre: ", 220, 20)
    movie_genre = function.place_entry(panel_option_admin, 20, 220, 40)

    lbl_movie_director = function.place_label(panel_option_admin, "Director: ", 420, 20)
    movie_director = function.place_entry(panel_option_admin, 20, 420, 40)

    lbl_movie_rating = function.place_label(panel_option_admin, "Rating: ", 620, 20)
    movie_rating = function.place_entry(panel_option_admin, 20, 620, 40)

    lbl_movie_rating = function.place_label(panel_option_admin, "Synopsis: ", 820, 20)
    movie_synopsis = function.place_entry(panel_option_admin, 20, 820, 40)

    btn = function.place_button(panel_option_admin, "Add", "Blue", lambda: add_movie(
        window_admin, movie_name, movie_genre, movie_director, movie_rating, movie_synopsis ), 20, 100)     # button to add movies/series to the catalog
    btn = function.place_button(panel_option_admin, "Reset", "Red", lambda: reset_movie(
        movie_name, movie_genre, movie_director, movie_rating, movie_synopsis), 60, 100)    #button to reset the whole section of entries 

    btn = function.place_button(panel_option_admin, "Remove Selected", "Red", lambda: del_movie(
        catalog_movie_admin, window_admin), 100, 100)       # button to remove movies/series from the catalog
    window_admin.mainloop()


def add_movie(window_admin: Misc, movie: Entry, genre: Entry, director: Entry, rating: Entry,synopsis: Entry):      # add movies/series function
    save = movie.get() + ";" + genre.get() + ";" + \
        director.get() + ";" + rating.get() + synopsis.get() + "\n"
    with open("database/movies.csv", "a", encoding="UTF-8") as f:  # append the new data
        f.write(save)
    messagebox.showinfo(title="Sucess", message="Movie successfully added", parent=window_admin)        # succes pop-up
    window_admin.destroy()
    admin_menu()

def del_movie(catalog_movie_admin: ttk.Treeview, window_admin: Misc):       # remove movies/series function
    selected_to_remove = catalog_movie_admin.focus()
    selected_to_remove = int(selected_to_remove[1:])
    i = 0
    with open("database/movies.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
        new_text = ""
        for line in f:
            i += 1
            movie = line.split(";")
            if selected_to_remove == i:
                print("removed")
            else:
                new_text = new_text + line
    with open("database/movies.csv", "w", encoding="UTF-8") as f:      # re-write the data
        f.write(new_text)
    messagebox.showinfo(title="Sucess", message="Movie successfully deleted", parent=window_admin)      # success pop-up
    window_admin.destroy()
    admin_menu()


def reset_movie(movie: Entry, genre: Entry, director: Entry, rating: Entry, synopsis: Entry):       # reset function
    movie.delete(0, END)
    genre.delete(0, END)
    director.delete(0, END)
    rating.delete(0, END)
    synopsis.delete(0, END)
