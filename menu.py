from tkinter import END, Button, Frame, Label, LabelFrame, Listbox, Menu, Menubutton, Misc, PanedWindow, Scrollbar, mainloop, messagebox, ttk, filedialog
import tkinter as tk
from typing import List
from PIL import Image, ImageTk
import function
import datetime
import menu_admin
import users
import interface_movie
import time



file_movies = "database\\movies.csv"
file_users = "database\\users.csv"

# writes on the "users.csv" the last time the user was online (Time/Date)LL


def last_session(user_id):          # last session registration function
    # open the file to read and to compare the user id with the data
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_text = ""
        for line in f:
            user = line.split(";")
            if user_id == user[0]:
                calender = datetime.datetime.now()
                time = datetime.datetime.now().time()
                # change the data to the year/month/day + hour/minute at the moment
                user[7] = calender.strftime("%Y%m%d") + time.strftime("%H%M")
                new_text = new_text + ";".join(user)
            else:
                new_text = new_text + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:      # re-write the data
        f.write(new_text)
    exit()      # close the whole program


def notifications(user_id, Menu_bar: Menu, note_movie: list, cont):       # notifications function
    opcoes_menu = Menu(Menu_bar)
    if cont == 1:
        opcoes_menu.add_command(label="Nothing new")
    else:
        # will show the movies that were added since the last time the user was online
        for i in range(1, len(note_movie)):
            opcoes_menu.add_command(label="• New movie : %s" % (note_movie[i][1]), command=lambda i=i: interface_movie.movie_interface(user_id, int(note_movie[i][0])))
    Menu_bar.add_cascade(label="Notification %s" % (cont-1), menu=opcoes_menu)

    # open the file to read and to compare the user id with the data
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_text = ""
        for line in f:
            user = line.split(";")
            if user_id == user[0]:
                calender = datetime.datetime.now()
                time = datetime.datetime.now().time()
                # change the data to the year/month/day + hour/minute at the moment
                user[7] = calender.strftime("%Y%m%d") + time.strftime("%H%M")
                new_text = new_text + ";".join(user)
            else:
                new_text = new_text + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:      # re-write the data
        f.write(new_text)

        # btn_quit = function.place_button(note_window, "Quit", "black", note_window.destroy, 240, 290)ck", note_window.destroy, 240, 290)


def select(btn, listbox_gender_option: Listbox, panel_catalog_movie: PanedWindow, user_id: int, window_menu: Misc):
    gender = []
    gname = listbox_gender_option.curselection()
    for i in gname:
        op = listbox_gender_option.get(i)
        gender.append(op)
    window_menu.destroy()
    menu(user_id,gender)

def menu(user_id, gender: List = []):  # menu function
    window_menu = function.tk_window("MOVIETIME", "1600x1000", [1000, 650], [1600, 1000])      # Main window

    # top level bar with options for use by the user/admin
    Menu_bar = Menu(window_menu)

    Menu_bar.add_command(label="User Perfil", command=lambda: users.perfil(user_id))      # top level bar option

    # top level bar for exclusive use by the admin/admins
    window_menu.configure(menu=Menu_bar)

    # open the file to read and to compare the user id with the data
    user_last_session = ""
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            words = line.split(";")
            if user_id == words[0]:
                user_last_session = words[7]
            # if the condition it's true, goes to the admin configure window of the main page
            if words[5] == "admin" and user_id == words[0]:
                Menu_bar.add_command(label="Admin Configs", command=menu_admin.admin_menu)

    cont = 0
    note_movie = []
    # open the file to read the movies data
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        for line in f:
            movies = line.split(";")
            # analyzes if the movie publishment date is greater than the date of the last user activity
            if user_last_session < movies[7]:
                note_movie.append([movies[0], movies[1]])
                cont += 1
    notifications(user_id, Menu_bar, note_movie, cont)
    Menu_bar.add_command(label="Quit", command=lambda: last_session(user_id))       # top level bar option

    label_mamado = function.place_label_frame(window_menu, "Gender", 100, 200, 10, 10)

    scrollbar = Scrollbar(label_mamado)
    scrollbar.pack(side='right', fill='y')

    listbox_gender_option = Listbox(label_mamado, yscrollcommand=scrollbar.set, selectmode="multiple")

    listbox_gender_option.pack(side='left', fill='both')
    scrollbar.config(command=listbox_gender_option.yview)

    panel_catalog_movie = function.panel_window(window_menu, 1200, 830, 250, 20)

    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    movie_cat_list = []
    for i in range(1, len(lines)):
        movie_cat = lines[i].split(";")
        if movie_cat[3] not in movie_cat_list:
            movie_cat_list.append(movie_cat[3])
    for i in range(len(movie_cat_list)):
        listbox_gender_option.insert(END, movie_cat_list[i])

    btn_filter = function.place_button(window_menu, "Filter", "black", lambda : select(btn, listbox_gender_option, panel_catalog_movie, user_id, window_menu), 65, 200)


    with open(file_movies, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    movie_list = []
    if len(gender) != 0:
        movie_list.append("Id;Movies;Picture;Genres;Director;Rating;Synopsis;Time;Empty Space")
    for line in lines:
        movie_info = line.split(";")
        if (movie_info[3] in gender) or (len(gender) == 0):
            movie_list.append(line)

    image_dimentions = [160, 160]
    btn = []
    poster = []
    id_movie = []
    for i in range(1, len(movie_list)):
        info_movie = movie_list[i].split(";")
        btnImage = Image.open(info_movie[2])
        btnImage = btnImage.resize((image_dimentions[0], image_dimentions[1]), Image.ANTIALIAS)
        btnImage2 = ImageTk.PhotoImage(btnImage)
        poster.append(btnImage2)
        id_movie.append(int(info_movie[0]))
        function.button_img(panel_catalog_movie, poster[i-1], lambda i=i: interface_movie.movie_interface(user_id, id_movie[i-1]), image_dimentions[0], image_dimentions[1], 10+(200*((i-1) % 5)), 10+(200*((i-1)//5)))

    window_menu.mainloop()

menu("2")