from email.encoders import encode_noop
from site import USER_SITE
from tkinter import Label, Menu, Misc, Text
from tkinter.constants import DISABLED, END, LEFT, RIGHT, SUNKEN, TOP
from tkinter.ttk import Treeview
import datetime

from PIL import Image, ImageTk

import function

from database import get_movie_metadata_as_list, increment_movie_view_count, get_movie_metadata

MOVIE_RATING_COUNT_INDEX = 8
MOVIE_RATING_SUM_INDEX = 9


def save_comments(entry_comments: Text, id_movie: int, id_user: int):
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    user = []
    for i in range(1, len(lines)):
        user = lines[i].split(";")
        if user[0] == id_user:
            break
    with open("comments/%s.csv" % (id_movie), "r", encoding="UTF-8") as f:
        lines = f.readlines()
    with open("comments/%s.csv" % (id_movie), "w", encoding="UTF-8") as f:
        for i in range(len(lines)):
            f.write(lines[i])
        f.write("(%s %s) %s : %s\n\n" % (datetime.datetime.now().strftime(
            "%H:%M"), datetime.datetime.now().strftime("%d/%m/%Y"), user[1], entry_comments.get("1.0", END).rstrip()))

def favorite_add(id_user, movie: list, window_movie: Misc, id_movie):
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_txt = ""
        for line in f:
            users = line.split(";")
            if users[0] == id_user:
                if users[9] == "None\n":
                    users[9] = movie[1] + "\n"
                    new_txt = new_txt + ";".join(users)
                else:
                    user_fav_strip = users[9].strip("\n")
                    user_fav = user_fav_strip.split("%") 
                    user_fav.append(movie[1])
                    user_fav.sort()
                    users[9] = "%".join(user_fav) + "\n"
                    new_txt = new_txt + ";".join(users)
            else:
                new_txt = new_txt + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:
        f.write(new_txt)
        
    window_movie.destroy()
    movie_interface(id_user, id_movie)

def favorite_del(id_user, movie: list, window_movie: Misc, id_movie):       
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_txt = ""
        for line in f:
            users = line.split(";")
            if users[0] == id_user:
                user_fav_strip = users[9].strip("\n")
                user_fav = user_fav_strip.split("%")
                user_fav2 = []
                for movie_not_remove in user_fav:
                    if movie_not_remove != movie[1]:
                        user_fav2.append(movie_not_remove) 
                        user_fav2.sort()
                users[9] = "%".join(user_fav2) 
                new_txt = new_txt + ";".join(users)
            else:
                new_txt = new_txt + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:
        f.write(new_txt)

    window_movie.destroy()
    movie_interface(id_user, id_movie)

def view_add(id_user, movie, window_movie, id_movie):
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_txt = ""
        for line in f:
            users = line.split(";")
            if users[0] == id_user:
                if users[10] == "None\n":
                    users[10] = movie[1] + "\n"
                    new_txt = new_txt + ";".join(users)
                else:
                    user_view_strip = users[10].strip("\n")
                    user_view = user_view_strip.split("%") 
                    user_view.append(movie[1])
                    user_view.sort()
                    users[10] = "%".join(user_view) + "\n"
                    new_txt = new_txt + ";".join(users)
            else:
                new_txt = new_txt + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:
        f.write(new_txt)
        
    window_movie.destroy()
    movie_interface(id_user, id_movie)

def view_del(id_user, movie, window_movie, id_movie):
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_txt = ""
        for line in f:
            users = line.split(";")
            if users[0] == id_user:
                user_view_strip = users[10].strip("\n")
                user_view = user_view_strip.split("%")
                user_view2 = []
                for movie_not_remove in user_view:
                    if movie_not_remove != movie[1]:
                        user_view2.append(movie_not_remove) 
                        user_view2.sort()
                users[10] = "%".join(user_view2) + "\n"
                new_txt = new_txt + ";".join(users)
            else:
                new_txt = new_txt + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:
        f.write(new_txt)

    window_movie.destroy()
    movie_interface(id_user, id_movie)

def movie_interface(id_user: int, id_movie: int):
    print(f'What ID is this? {id_movie}')
    window_movie = function.toplevel_window("MOVIETIME", "1400x800")
    movie = get_movie_metadata_as_list(id_movie)
    movie_metadata = get_movie_metadata(id_movie)
    increment_movie_view_count(id_movie)

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

    movie_rating = "No Rating"

    if len(movie) > 9:
        try:
            movie_rating_count = int(movie[MOVIE_RATING_COUNT_INDEX])
            movie_rating_sum = int(movie[MOVIE_RATING_SUM_INDEX])
        except ValueError:
            movie_rating_count = 0
            movie_rating_sum = 0
        if movie_rating_count > 0:
            movie_rating = "%.2f" % (movie_rating_sum / movie_rating_count)

    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            users = line.split(";")
            if users[0] == id_user:
                users[9] = users[9].strip("\n")
                users_fav = users[9].split("%")
                if movie[1] not in users_fav:
                    btn_favorite_add = function.place_button(window_movie, "Add to Favorite List", "blue", lambda: favorite_add(id_user, movie, window_movie, id_movie), 1200, 100)
                else:
                    btn_favorite_remove = function.place_button(window_movie, "Remove from Favorite List", "red", lambda: favorite_del(id_user, movie, window_movie, id_movie), 1200, 100)

    movie_rating_label = Label(window_movie, text=f"Rating: {movie_rating}")
    movie_rating_label.place(x=1200, y=150)
    movie_rating_label.pack()

    movie_view_count = movie_metadata.get("View Count")
    if not movie_view_count:
        movie_view_count = 0
    
    movie_view_count_label = Label(window_movie, text=f"Views: {movie_view_count}")
    movie_view_count_label.pack()

    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            users = line.split(";")
            if users[0] == id_user:
                users[10] = users[10].strip("\n")
                users_fav = users[10].split("%")
                if movie[1] not in users_fav:
                    btn_view_add = function.place_button(window_movie, "Already Seen", "blue", lambda: view_add(id_user, movie, window_movie, id_movie), 1200, 50)
                else:
                    btn_view_remove = function.place_button(window_movie, "Not Seen", "red", lambda: view_del(id_user, movie, window_movie, id_movie), 1200, 50)
    
    try:
        with open("comments/%s.csv" % (id_movie), "r", encoding="UTF-8") as f:
            lines_comments = f.readlines()
    except FileNotFoundError:
        lines_comments = []

    list_entry_comments = function.place_text(window_movie, 80, 10, 1, 150)

    btn_entry_comments = function.place_button(window_movie, "Invite comment", "black", lambda: save_comments(
        list_entry_comments, id_movie, id_user), 1, 1)

    list_comments = function.place_text(window_movie, 80, 100, 1, 400)
    for i in range(len(lines_comments)):
        list_comments.insert(END, lines_comments[i])
    list_comments.config(state=DISABLED)
    
    window_movie.mainloop()


#movie_interface(2, 2)
