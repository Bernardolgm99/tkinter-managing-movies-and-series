from ast import Str
from tkinter import Button, Entry, Misc, filedialog, messagebox, ttk
from tkinter.constants import END

import function
import datetime

def admin_menu():
    window_admin = function.toplevel_window("MOVIETIME Admin", "950x600")
    window_admin.grab_set()
    panel_calog_movie_admin = function.panel_window(window_admin, 900, 231, 20, 20)
    catalog_movie_admin = function.catalog_view(panel_calog_movie_admin, ["Movie", "Genres", "Director", "Rating"], [200, 242, 200, 250])   # panel that shows the existent movies/series
    with open("database/movies.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
        for line in f:
            words = line.split(";")
            catalog_movie_admin.insert("", "end", values=(
                words[1], words[3], words[4], words[5]))        # inserts the whole data in movies.csv by lines

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

    lbl_img_dir = function.place_label(panel_option_admin, "Image directory: ", 100, 140)
    lbl_movie_dir = function.place_entry(panel_option_admin, 30, 100, 160)

    movie_dir = ""
    btn_img = function.place_button(panel_option_admin, "Add Image:", "black",lambda: img_catalog(movie_dir, panel_option_admin, lbl_movie_dir), 20, 155)


    btn = function.place_button(panel_option_admin, "Add", "Blue", lambda: add_movie(
        window_admin, movie_name, movie_genre, movie_director, movie_rating, movie_synopsis, lbl_movie_dir), 20, 100)     # button to add movies/series to the catalog
    btn = function.place_button(panel_option_admin, "Reset", "Red", lambda: reset_movie(
        movie_name, movie_genre, movie_director, movie_rating, movie_synopsis), 60, 100)    #button to reset the whole section of entries 

    btn = function.place_button(panel_option_admin, "Remove Selected", "Red", lambda: del_movie(
        catalog_movie_admin, window_admin), 100, 100)       # button to remove movies/series from the catalog
    window_admin.mainloop()

def img_catalog(movie_dir: str, panel_option_admin: Misc, lbl_movie_dir: Entry):
    movie_dir = filedialog.askopenfilename(initialdir="./", title="Select The Catalog Image", parent= panel_option_admin, filetypes=
                                    (("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("tiff files", "*.tiff")))
    lbl_movie_dir.insert(0, str(movie_dir))


def add_movie(window_admin: Misc, movie: Entry, genre: Entry, director: Entry, rating: Entry,synopsis: Entry, lbl_movie_dir: Entry):      # add movies/series function
    calender = datetime.datetime.now()
    time = datetime.datetime.now().time()
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        cont_line = f.readlines()
    save = str(len(cont_line)) + ";" + movie.get() + ";" + lbl_movie_dir.get() + ";" + genre.get() + ";" + director.get() + ";" + rating.get() + ";" + synopsis.get() + " " +  ";" + calender.strftime("%Y%m%d") + time.strftime("%H%M") + ";" + " " + "\n"
    with open("database/movies.csv", "a", encoding="UTF-8") as f:  # append the new data
        f.write(save)
    messagebox.showinfo(title="Sucess", message="Movie successfully added", parent=window_admin)        # succes pop-up
    window_admin.destroy()
    admin_menu()

def del_movie(catalog_movie_admin: ttk.Treeview, window_admin: Misc):       # remove movies/series function
    selected_to_remove = catalog_movie_admin.focus()
    selected_to_remove = int(selected_to_remove[1:], 16)
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





