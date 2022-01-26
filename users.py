from distutils import command
from email.encoders import encode_noop
from msilib.schema import ComboBox
from multiprocessing import Event
from optparse import Values
import tkinter
from tkinter.tix import IMAGETEXT
from unicodedata import category
import function
from PIL import Image, ImageTk

from tkinter import SUNKEN, TOP, Label, Misc, OptionMenu, StringVar, filedialog, messagebox, PhotoImage, ttk, Scrollbar, Listbox, END

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
            var_user = ""
            if txt_new_pw == "" and txt_new_repw == "":
                messagebox.showerror(title="Warning!",message="You need to type something!")      # warning pop-up
                return
            else:
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

def category_changed(chosen_cat: StringVar, user_id): # function to change the favorite category
    messagebox.showinfo(title="Change Result", message="You succesfully changed your favorite category to: {0}".format(chosen_cat.get()))
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        new_text = ""
        for line in f:
            users = line.split(";")
            if users[0] == user_id:
                users[8] = chosen_cat.get()
                new_text = new_text + ";".join(users)
            else:
                new_text = new_text + line
    with open("database/users.csv", "w", encoding="UTF-8") as f:
        f.write(new_text)

def perfil(user_id):        # user perfil based on his id function
    perfil_window = function.toplevel_window("Perfil", "600x800")
    perfil_window.configure(background="#E0ECE4")

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
                try:
                    img = Image.open(user_line[6])      # show the profile picture selected (or default) by the user
                except FileNotFoundError:
                    img = Image.new("RGB", (160, 160))
                resized_img_1 = img.resize((200,200), Image.ANTIALIAS)      #resize the image
                img_1 = ImageTk.PhotoImage(resized_img_1)       
                label = Label(perfil_window, image=img_1, bd=5, relief=SUNKEN)      #label where the picture will appear
                label.pack(padx=2, pady=2, side=TOP)
                break
        else:
            return None

    
    #group of labels and entries
    lbl_fname = function.place_label(
        perfil_window, "First Name: ", 100, 250, "grey")
    lbl_lname = function.place_label(
        perfil_window, "Last Name: ", 300, 250, "grey")
    lbl_email = function.place_label(
        perfil_window, "Email:", 100, 300, "grey")
    lbl_new_pw = function.place_label(
        perfil_window, "Change your password (Optional): ", 100, 350, "grey")
    lbl_new_repw = function.place_label(
        perfil_window, "Re-enter your password: ", 100, 400, "grey")
    txt_fname = function.place_label(
        perfil_window, first_name, 170, 250, "black")
    txt_lname = function.place_label(
        perfil_window, last_name, 370, 250, "black")
    txt_email = function.place_label(
        perfil_window, email, 150, 300, "black")
    txt_new_pw = function.place_entry(
        perfil_window, 27, 290, 350, "*")
    txt_new_repw = function.place_entry(
        perfil_window, 27, 235, 400, "*")

    #Combobox
    with open("database/movies.csv", "r", encoding="UTF-8") as f:
        category_list = []
        for line in f:
            movies = line.split(";")
            if movies[3] != "Genres":
                if movies[3] not in category_list:
                    category_list.append(movies[3])
    
    lbl_choose_cat = function.place_label(perfil_window, "Choose your favorite category: ", 130, 500, "grey")

    chosen_cat = tkinter.StringVar()
    cb_categories = ttk.Combobox(perfil_window, values = category_list, textvariable=chosen_cat)
    cb_categories.place(x=300, y=500)
    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            users = line.split(";")
            if users[0] == user_id:
                if users[8] != "None\n":
                    cb_categories.set(users[8])

    btn_cb_categories = function.place_button(perfil_window, "Confirm Change", "red", lambda: category_changed(chosen_cat, user_id), 300, 550)

    #Listbox
    lbl_scroll = function.place_label_frame(perfil_window, "Favorite Movies", 150, 200, 100, 600)

    scrollbar = Scrollbar(lbl_scroll)
    scrollbar.pack(side='right', fill='y')

    listbox_movie_option = Listbox(lbl_scroll, yscrollcommand=scrollbar.set, selectmode="multiple")

    listbox_movie_option.pack(side='left', fill='both')
    scrollbar.config(command=listbox_movie_option.yview)

    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            users = line.split(";")
            # analyzes if the movie publishment date is greater than the date of the last user activity
            if users[0] == user_id:
                if users[9] != "None\n":
                    user_fav_strip = users[9].strip("\n")
                    user_fav = user_fav_strip.split("%")
                    for i in range(int(len(user_fav))):
                        listbox_movie_option.insert(END, user_fav[i])

    #Listbox
    lbl_scroll_vist = function.place_label_frame(perfil_window, "Movies I Saw", 150, 200, 350, 600)

    scrollbar = Scrollbar(lbl_scroll_vist)
    scrollbar.pack(side='right', fill='y')

    listbox_vist_option = Listbox(lbl_scroll_vist, yscrollcommand=scrollbar.set, selectmode="multiple")

    listbox_vist_option.pack(side='left', fill='both')
    scrollbar.config(command=listbox_vist_option.yview)

    with open("database/users.csv", "r", encoding="UTF-8") as f:
        for line in f:
            users = line.split(";")
            # analyzes if the movie publishment date is greater than the date of the last user activity
            if users[0] == user_id:
                if users[10] != "None\n":
                    user_view_strip = users[10].strip("\n")
                    user_view = user_view_strip.split("%")
                    for i in range(int(len(user_view))):
                        listbox_vist_option.insert(END, user_view[i])

    btn_avatar = function.place_button(         
        perfil_window, "New Profile Pic", "blue", lambda:image (perfil_window, user_id), 20, 20)    #button to change the profile picture 
    btn_new_pw = function.place_button(
        perfil_window, "Change Password", "red", lambda: new_pw (user_id, txt_new_pw.get(), txt_new_repw.get()), 150, 450)      #button to change the password if the user wants to
    
    perfil_window.mainloop()
