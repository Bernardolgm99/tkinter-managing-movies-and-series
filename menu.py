from tkinter import *  # type: ignore
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import function
import datetime
import menu_admin


def image():
    filename = filedialog.askopenfilename(title="Select file", filetypes=(
        ("jpg files", ".jpg"), ("png files", ".png"), ("jpeg files", ".jpeg"), ("tiff files", ".tiff")))


def perfil(user_id):
    perfil_window = function.toplevel_window("Perfil", "600x800")
    global img_1
    img_1 = PhotoImage(name="user", file="user.png")
    label = Label(perfil_window, image=img_1, bd=5, relief=SUNKEN)
    label.pack(padx=10, pady=10, side=RIGHT)

    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            user_line = line.split(";")
            if user_id == user_line[0]:
                # writes a label on the perfil saying the users first name
                first_name = user_line[1]
                # writes a label on the perfil saying the users last name
                last_name = user_line[2]
                # writes a label on the perfil saying the users email
                email = user_line[3]

    lbl_fname = function.place_label(
        perfil_window, "First Name: ", 100, 100, "grey")
    lbl_lname = function.place_label(
        perfil_window, "Last Name: ", 200, 200, "grey")
    lbl_email = function.place_label(perfil_window, "Email:", 300, 300, "grey")

    btn_avatar = function.place_button(
        perfil_window, "New Profile Pic", "blue", image, 400, 400)

# writes on the "users.csv" the last time the user was online (Time/Date)LL


def last_session(user_id):
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_text = ""
        for line in f:
            user = line.split(";")
            if user_id == user[0]:
                calender = datetime.datetime.now()
                time = datetime.datetime.now().time()
                user[6] = calender.strftime("%Y%m%d") + time.strftime("%H%M")
                new_text = new_text + ";".join(user)
            else:
                new_text = new_text + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:
        f.write(new_text)
    exit()


def menu(user_id):  # menu
    window_menu = function.tk_window(
        "MOVIETIME", "1000x650", [1000, 650], [1000, 650])

    Menu_bar = Menu(window_menu)

    Menu_bar.add_command(label="User Perfil", command=lambda: perfil(user_id))

    window_menu.configure(menu=Menu_bar)
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            words = line.split(";")
            if words[5] == "admin" and user_id == words[0]:
                Menu_bar.add_command(label="Admin Configs", command=menu_admin.admin_menu)

    Menu_bar.add_command(label="Quit", command=lambda: last_session(user_id))

    panel = PanedWindow(window_menu, width=450, height=270, bd="3", relief="sunken")
    panel.place(x=0, y=0)
    tree = function.catalog_view(panel, ("Nome", "Email", "Senha", "Tipo"), (100, 100, 100, 150))  # type: ignore
