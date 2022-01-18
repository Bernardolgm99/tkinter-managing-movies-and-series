from ast import List
from logging import info
from msilib.schema import ListBox
from pydoc import text
from textwrap import fill, wrap
from tkinter import ANCHOR, END, VERTICAL, Button, Frame, Label, LabelFrame, Listbox, Menu, Menubutton, Misc, Scrollbar, mainloop, messagebox, ttk, filedialog
import tkinter as tk
from turtle import width, write_docstringdict
from unittest import result
from PIL import Image, ImageTk
import function
import datetime
import menu_admin
import users
import interface_movie

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
    note_window = function.tk_window("NOTIFICATIONS", "400x300", [400, 300], [400, 300])

    x = 10
    y = 20 
    x_flbl = 5
    y_flbl = 10

    if cont == 0:
        frame_lbl_noti = function.place_label_frame(note_window,"", 350, 40, 5, 10)
        lbl_noti = function.place_label(note_window,"• 0 movies were added since your last session, come back later!", 10, 20)
    else:
        # write code to show up new movies

        for i in range (len(note_movie)):       # will show the movies that were added since the last time the user was online
            frame_lbl_noti = function.place_label_frame(note_window,"", 350, 40, x_flbl, y_flbl)        # places a label frame
            lbl_noti = function.place_label(note_window, ("• The movie {0} was added.".format(note_movie[i])), x, y)
            y+=40
            y_flbl+=40

        with open("database/users.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
            new_text = ""
            for line in f:
                user = line.split(";")
                if user_id == user[0]:
                    calender = datetime.datetime.now()
                    time = datetime.datetime.now().time()
                    user[7] = calender.strftime("%Y%m%d") + time.strftime("%H%M")       # change the data to the year/month/day + hour/minute at the moment
                    new_text = new_text + ";".join(user)
                else:
                    new_text = new_text + line
        with open("database/users.csv", "w", encoding="UTF-8") as f:      # re-write the data
            f.write(new_text)

        #btn_quit = function.place_button(note_window, "Quit", "black", note_window.destroy, 240, 290)

def select(btn, listbox_gender_option: Listbox):  
    gender = []
    gname = listbox_gender_option.curselection()
    for i in gname:
        op = listbox_gender_option.get(i)
        gender.append(op)
    for i in range (len(btn)):
        btn[i].destroy()


def menu(user_id):  # menu function
    window_menu = function.tk_window("MOVIETIME", "1600x1000", [1000, 650], [
                                     1600, 1000])      # Main window

    # top level bar with options for use by the user/admin
    Menu_bar = Menu(window_menu)

    Menu_bar.add_command(label="User Perfil", command=lambda: users.perfil(
        user_id))      # top level bar option

    # top level bar for exclusive use by the admin/admins
    window_menu.configure(menu=Menu_bar)

    with open("database/users.csv", "r", encoding="UTF-8") as f:        # open the file to read and to compare the user id with the data
        for line in f:
            words = line.split(";") 
            if user_id == words[0]:
                user_last_session = words[7]
            if words[5] == "admin" and user_id == words[0]:     # if the condition it's true, goes to the admin configure window of the main page
                Menu_bar.add_command(label="Admin Configs",
                                     command=menu_admin.admin_menu)
            
    cont = 0
    note_movie = []
    with open("database/movies.csv", "r", encoding="UTF-8") as f:       # open the file to read the movies data
        for line in f:
            movies = line.split(";")
            if user_last_session < movies[7]:   # analyzes if the movie publishment date is greater than the date of the last user activity
                note_movie.append(movies[1])
                cont+=1
    if cont == 0:
        Menu_bar.add_command(label="Notifications", command=lambda: notifications(user_id, Menu_bar, note_movie, cont))
    else:
        Menu_bar.add_command(label="Notifications  {0}".format(cont), command=lambda: notifications(user_id, Menu_bar, note_movie, cont))

    Menu_bar.add_command(label="Quit", command=lambda: last_session(
        user_id))       # top level bar option

    label_mamado = function.place_label_frame(window_menu, "Gender", 100, 200, 10,10)

    scrollbar = Scrollbar(label_mamado)
    scrollbar.pack( side = 'right', fill = 'y' )

    listbox_gender_option = Listbox(label_mamado, yscrollcommand = scrollbar.set, selectmode= "multiple")

    listbox_gender_option.pack( side = 'left', fill = 'both' )
    scrollbar.config( command = listbox_gender_option.yview )

    panel_catalog_movie = function.panel_window(
        window_menu, 1200, 830, 250, 20)
    
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    movie_cat_list = []
    for i in range (1,len(lines)):
        movie_cat = lines[i].split(";")
        if movie_cat[3] not in movie_cat_list:
            movie_cat_list.append(movie_cat[3])
    for i in range (len(movie_cat_list)):
        listbox_gender_option.insert(END, movie_cat_list[i])

    btn_filter = function.place_button(window_menu, "Filter", "black", lambda: select(btn, listbox_gender_option), 65, 200)
    

    with open(file_movies, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    image_dimentions = [160, 160]
    btn = []
    poster = []
    id_movie = []
    for i in range(1, len(lines)):
        info_movie = lines[i].split(";")
        btnImage = Image.open(info_movie[2])
        btnImage = btnImage.resize(
            (image_dimentions[0], image_dimentions[1]), Image.ANTIALIAS)
        btnImage2 = ImageTk.PhotoImage(btnImage)
        poster.append(btnImage2)
        id_movie.append(int(info_movie[0]))
        btn.append(function.button_img(panel_catalog_movie, poster[i-1], lambda i=i: interface_movie.movie_interface(
            user_id, id_movie[i-1]), image_dimentions[0], image_dimentions[1], 10+(200*((i-1) % 5)), 10+(200*((i-1)//5))))

    window_menu.mainloop()


menu("2") 