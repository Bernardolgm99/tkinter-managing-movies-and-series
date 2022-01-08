from tkinter import Label
from tkinter.constants import DISABLED, END, LEFT, RIGHT, SUNKEN, TOP
from tkinter.ttk import Treeview

from PIL import Image, ImageTk

import function


def movie_interface(user_id: int, movie_list: Treeview):
    window_movie = function.toplevel_window("MOVIETIME")
    selected = 2
    #selected = int(selected[1:],16)
    i = 0
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        movie = []
        for i, line in enumerate(f, start = 1):
            if selected == i:
                movie = line.split(";")
                break
        else:
            # Só executa o ele se não ativar o break
            return None

    title_movie = function.place_label(window_movie,str(movie[0]),0,0,font="Verdana 40")
    title_movie.pack(side=TOP)
    img_movie_resized = function.place_img(window_movie,movie[1])

    label_img_movie = Label(window_movie, image=img_movie_resized, bd=0, relief=SUNKEN)
    label_img_movie.pack(padx=10, pady=10, side=RIGHT)

    synopsis_movie = function.place_text(window_movie, 60, 10, 20, 110)
    synopsis_movie.insert(END,movie[5])
    synopsis_movie.config(state=DISABLED, bg="#f0f0f0")
    
    window_movie.mainloop()

movie_interface(2, Treeview())
