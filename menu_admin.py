from tkinter import * #type: ignore
import function

def admin_menu():
    window_admin = function.tk_window("800x600","MOVIETIME Admin","zoomed")
    panel_calog_movie_admin = function.panel_window(window_admin,900,231,20,20)
    catalog_movie_admin = function.catalog_view(panel_calog_movie_admin,("Movie","Genres","Director","Rating"),(200,242,200,250)) #type: ignore
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

    btn = function.place_button(panel_option_admin,"Add","Blue",lambda: add_movie(movie_name.get(),movie_genre.get(),movie_director.get(),movie_rating.get()),20,100)

    window_admin.mainloop()

def add_movie(movie: str,genre: str,director: str,rating: str):
    save =  movie + ";" + genre + ";" + director + ";" + rating + "\n"
    with open("database/movies.csv", "a", encoding="UTF-8") as f:  # append the new data
        f.write(save)