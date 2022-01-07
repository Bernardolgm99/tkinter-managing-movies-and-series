from tkinter import *
from tkinter.ttk import Treeview #type: ignore
import function
from PIL import ImageTk, Image

def movie_interface(user_id: int, movie_list: Treeview):
    window_movie = function.tk_window("MOVIETIME")
    selected_to_remove = 2
   # selected_to_remove = int(selected_to_remove[1:])
    i = 0
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        new_text = ""
        for line in f:
            i += 1
            if selected_to_remove == i:
                movie = line.split(";")
                break
    title_movie = function.place_label(window_movie,str(movie[0]),0,0,font="Verdana 40")
    title_movie.pack()
    
    #label_img_movie = function.place_img(window_movie,movie[5],LEFT)
    img_movie = Image.open(movie[1])
    resized = img_movie.resize((338,500), Image.ANTIALIAS)
    img_movie_resized = ImageTk.PhotoImage(resized)

    label_img_movie = Label(window_movie, image=img_movie_resized, bd=5, relief=SUNKEN)
    label_img_movie.pack(padx=10, pady=10, side=RIGHT)
    
    synopsis_movie = function.place_text(window_movie, 60, 10, 20, 110)
    synopsis_movie.insert(END,movie[5])
    synopsis_movie.config(state=DISABLED, bg="#f0f0f0")
    
    window_movie.mainloop()

movie_interface(2, 1)