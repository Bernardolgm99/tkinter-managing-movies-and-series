from tkinter import Label, Text
from tkinter.constants import DISABLED, END, LEFT, RIGHT, SUNKEN, TOP
from tkinter.ttk import Treeview
import datetime

from PIL import Image, ImageTk

import function


def save_comments(entry_comments: Text, id_movie: int, id_user: int):
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    user = []
    for i in range(1, len(lines)):
        user = lines[i].split(";")
        if int(user[0]) == id_user:
            break
    with open("comments/%s.csv" % (id_movie), "r", encoding="UTF-8") as f:
        lines = f.readlines()
    with open("comments/%s.csv" % (id_movie), "w", encoding="UTF-8") as f:
        for i in range(len(lines)):
            f.write(lines[i])
        f.write("(%s %s) %s : %s\n\n" % (datetime.datetime.now().strftime(
            "%H:%M"), datetime.datetime.now().strftime("%d/%m/%Y"), user[1], entry_comments.get("1.0", END).rstrip()))


def movie_interface(user_id: int, id_movie: int):
    window_movie = function.toplevel_window("MOVIETIME", "1400x800")
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        movie = []
        for i, line in enumerate(f, start=1):
            if (id_movie+1) == i:
                movie = line.split(";")
                break
        else:
            # Só executa o ele se não ativar o break
            return None

    title_movie = function.place_label(
        window_movie, str(movie[1]), 0, 0, font="Verdana 40")
    title_movie.pack(side=TOP)
    img_movie_resized = function.place_img(window_movie, movie[2])

    label_img_movie = Label(
        window_movie, image=img_movie_resized, bd=0, relief=SUNKEN)
    label_img_movie.pack(padx=10, pady=10, side=RIGHT)

    synopsis_movie = function.place_text(window_movie, 60, 10, 20, 110)
    synopsis_movie.insert(END, movie[6])
    synopsis_movie.config(state=DISABLED, bg="#f0f0f0")

    with open("comments/%s.csv" % (id_movie), "r", encoding="UTF-8") as f:
        lines_comments = f.readlines()

    list_entry_comments = function.place_text(window_movie, 80, 10, 1, 150)

    btn_entry_comments = function.place_button(window_movie, "Invite comment", "black", lambda: save_comments(
        list_entry_comments, id_movie, user_id), 1, 1)

    list_comments = function.place_text(window_movie, 80, 100, 1, 400)
    for i in range(len(lines_comments)):
        list_comments.insert(END, lines_comments[i])
    list_comments.config(state=DISABLED)
    window_movie.mainloop()


movie_interface(2, 2)
