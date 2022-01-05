from tkinter import *
from tkinter import messagebox
import function

def admin_menu():
    window_admin = function.tk_window("800x600","MOVIETIME Admin","zoomed")
    panel_calog_movie_admin = function.panel_window(window_admin,900,231,20,20)
    catalog_movie_admin = function.catalog_view(panel_calog_movie_admin,("Movie","Genres","Director","Rating"),(200,242,200,250))
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        for line in f:
            words = line.split(";")
            catalog_movie_admin.insert("", "end", values = (words[0], words[1],words[2],words[3]))

    panel_option_admin = function.panel_window(window_admin,900,200,20,300)

    lbl_movie_name = function.place_label(panel_option_admin,"Movie Name: ",20,20)
    movie_name = function.place_entry(panel_option_admin,20,20,40)

    lbl_movie_genre = function.place_label(panel_option_admin,"Genre: ",220,20)
    movie_genre = function.place_entry(panel_option_admin,20,220,40)

    lbl_movie_director = function.place_label(panel_option_admin,"Director: ",420,20)
    movie_director = function.place_entry(panel_option_admin,20,420,40)

    lbl_movie_rating = function.place_label(panel_option_admin,"Rating: ",620,20)
    movie_rating = function.place_entry(panel_option_admin,20,620,40)

    btn = function.place_button(panel_option_admin,"Add","Blue",lambda: add_movie(panel_calog_movie_admin,catalog_movie_admin, movie_name,movie_genre,movie_director,movie_rating),20,100)
    btn = function.place_button(panel_option_admin,"Reset","Red",lambda: reset_movie(movie_name,movie_genre,movie_director,movie_rating),60,100)

def add_movie(panel_calog_movie_admin, catalog, movie: Entry,genre: Entry,director: Entry,rating: Entry):
    save =  movie.get() + ";" + genre.get() + ";" + director.get() + ";" + rating.get() + "\n"
    with open("database/movies.csv", "a", encoding="UTF-8") as f:  # append the new data
        f.write(save)
    catalog = function.catalog_view(panel_calog_movie_admin,("Movie","Genres","Director","Rating"),(200,242,200,250))
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        for line in f:
            words = line.split(";")
            catalog.insert("", "end", values = (words[0], words[1],words[2],words[3]))
    reset_movie(movie, genre, director, rating)

def reset_movie(movie: Entry,genre: Entry,director: Entry,rating: Entry):
    movie.delete(0, END)
    genre.delete(0, END)
    director.delete(0, END)
    rating.delete(0, END)