from tkinter import *  # type: ignore
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import function
import datetime
import menu_admin


def image(perfil_window:Misc, user_id):             # perfil image selection function
    filename = filedialog.askopenfilename(initialdir="images",title="Select file", parent=perfil_window, filetypes=(
            ("all files", "*.*"), ("jpg files", ".jpg"), ("png files",".png")))
    if filename == "":      # condition if the user closes the "select file" window
        return()
    else:    
        with open("database/users.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data 
            new_text = ""
            for line in f:
                user = line.split(";")
                if user_id == user[0]:
                    user[6] = filename
                    new_text = new_text + ";".join(user)
                else:
                    new_text = new_text + line
        with open("database/users.csv", "w", encoding="UTF-8") as f:      # re-write the data 
            f.write(new_text)
        perfil_window.destroy()         #refresh the window to show the new profile picture
        perfil(user_id)

def new_pw(user_id, txt_new_pw: str, txt_new_repw: str):        # password change function 
    if txt_new_repw == txt_new_pw:          #condition needed to re-write the new password
        with open("database/users.csv", "r", encoding="UTF-8") as f:        # open the file to read and to compare the user id with the data
            new_text = ""
            for line in f:
                user = line.split(";")
                if user_id == user[0]:
                    if txt_new_pw == user[4]:
                        messagebox.showerror(title="Warning!",message="Your new password is the same as the old password, try again!")      # warning pop-up
                        var_user = user[4]      
                        break
                    messagebox.showinfo(title="Sucess", message="Your password has been changed!")      # success pop-up
                    var_user = user[4]
                    user[4] = txt_new_pw
                    new_text = new_text + ";".join(user)
                else:
                    new_text = new_text + line
        if txt_new_pw != var_user:
            with open("database/users.csv", "w", encoding="UTF-8") as f:        # re-write the data 
                f.write(new_text)
    else:
        messagebox.showerror(title="Warning!", message="The passwords must be the same!")       # error pop-up 

def perfil(user_id):        # user perfil based on his id function
    perfil_window = function.toplevel_window("Perfil", "600x800")

    with open("database/users.csv", "r", encoding="UTF-8") as f:        # open the file to read and to compare the user id with the data
        for line in f:
            user_line = line.split(";")
            if user_id == user_line[0]:     # condition based on the users id
                # writes a label on the perfil saying the users first name
                first_name = user_line[1]
                # writes a label on the perfil saying the users last name
                last_name = user_line[2]
                # writes a label on the perfil saying the users email
                email = user_line[3]
                global img_1
                img = Image.open(user_line[6])      # show the profile picture selected (or default) by the user
                resized_img_1 = img.resize((200,200), Image.ANTIALIAS)      #resize the image
                img_1 = ImageTk.PhotoImage(resized_img_1)       
                label = Label(perfil_window, image=img_1, bd=5, relief=SUNKEN)      #label where the picture will appear
                label.pack(padx=2, pady=2, side=TOP)

    #group of labels and entries
    lbl_fname = function.place_label(
        perfil_window, "First Name: ", 100, 250, "grey")
    lbl_lname = function.place_label(
        perfil_window, "Last Name: ", 300, 250, "grey")
    lbl_email = function.place_label(
        perfil_window, "Email:", 100, 300, "grey")
    lbl_new_pw = function.place_label(
        perfil_window, "Change your password (Optional): ", 100, 450, "grey")
    lbl_new_repw = function.place_label(
        perfil_window, "Re-enter your password: ", 100, 500, "grey")
    txt_fname = function.place_label(
        perfil_window, first_name, 170, 250, "black")
    txt_lname = function.place_label(
        perfil_window, last_name, 370, 250, "black")
    txt_email = function.place_label(
        perfil_window, email, 150, 300, "black")
    txt_new_pw = function.place_entry(
        perfil_window, 27, 290, 450, "*")
    txt_new_repw = function.place_entry(
        perfil_window, 27, 235, 500, "*")

    btn_avatar = function.place_button(         
        perfil_window, "New Profile Pic", "blue", lambda:image (perfil_window, user_id), 20, 20)    #button to change the profile picture 
    btn_new_pw = function.place_button(
        perfil_window, "Change Password", "red", lambda: new_pw (user_id, txt_new_pw.get(), txt_new_repw.get()), 150, 550)      #button to change the password if the user wants to
    
    perfil_window.mainloop()
# writes on the "users.csv" the last time the user was online (Time/Date)LL


def last_session(user_id):          # last session registration function
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
    exit()      # close the whole program


def menu(user_id):  # menu function
    window_menu = function.tk_window(
        "MOVIETIME", "1000x650", [1000, 650], [1000, 650])      # Main window

    Menu_bar = Menu(window_menu)        # top level bar with options for use by the user/admin

    Menu_bar.add_command(label="User Perfil", command=lambda: perfil(user_id))      # top level bar option 

    window_menu.configure(menu=Menu_bar)        # top level bar for exclusive use by the admin/admins
    with open("database/users.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
        for line in f:
            words = line.split(";")
            if words[5] == "admin" and user_id == words[0]:         # if the condition it's true, goes to the admin configure window of the main page
                Menu_bar.add_command(label="Admin Configs", command=menu_admin.admin_menu)

    Menu_bar.add_command(label="Quit", command=lambda: last_session(user_id))       # top level bar option 

    panel = PanedWindow(window_menu, width=450, height=270, bd="3", relief="sunken")        #main page panel displaying all the movies, series, etc.
    panel.place(x=0, y=0)
    tree = function.catalog_view(panel, ("Nome", "Email", "Senha", "Tipo"), (100, 100, 100, 150))  # type: ignore

    window_menu.mainloop()