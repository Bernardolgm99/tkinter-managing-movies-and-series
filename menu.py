from logging import info
from tkinter import Button, Menu, mainloop, messagebox, ttk, filedialog
import tkinter as tk
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

def notifications(window_menu: Misc, user_id, Menu_bar: Menu, note_movie: list):
    note_window = function.tk_window("NOTIFICATIONS", "400x300", [400, 300], [400, 300])
    
    # write code to show up new movies

    x = 10
    y = 20
    x_flbl = 5
    y_flbl = 10
    for i in range (len(note_movie)):
        frame_lbl_noti = function.place_label_frame(note_window,"", 350, 40, x_flbl, y_flbl)
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
    Menu_bar.entryconfig(3, label = "Notifications")

    #btn_quit = function.place_button(note_window, "Quit", "black", note_window.destroy, 240, 290)
       

def menu(user_id):  # menu function
    window_menu = function.tk_window("MOVIETIME", "1600x1000", [1000, 650], [
                                     1600, 1000])      # Main window

    # top level bar with options for use by the user/admin
    Menu_bar = Menu(window_menu)

    Menu_bar.add_command(label="User Perfil", command=lambda: users.perfil(
        user_id))      # top level bar option

    # top level bar for exclusive use by the admin/admins
    window_menu.configure(menu=Menu_bar)
    # open the file to read and to compare the user id with the data
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            words = line.split(";")
            # if the condition it's true, goes to the admin configure window of the main page
            if words[5] == "admin" and user_id == words[0]:
                Menu_bar.add_command(label="Admin Configs",
                                     command=menu_admin.admin_menu)

    Menu_bar.add_command(label="Quit", command=lambda: last_session(
        user_id))       # top level bar option

    # main page panel displaying all the movies, series, etc.
    panel_catalog_movie = function.panel_window(
        window_menu, 1200, 830, 250, 20)
    listbox_gender_option = function.listbox_panel(window_menu, 40, 20, 0, 20)

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
