from tkinter import *  # type: ignore
from tkinter import messagebox
import function
import menu
from PIL import ImageTk



# file to store functions 

global user_id


def reset_sign_in():  # reset function of Sign In
    txt_fname.delete(0, END)
    txt_lname.delete(0, END)
    txt_email.delete(0, END)
    txt_uppw.delete(0, END)
    txt_rpw.delete(0, END)


def reset_sign_up():  # reset function of Sign Up
    txt_pw.delete(0, END)
    txt_user.delete(0, END)


def sign_up():  # sign up function
    if txt_uppw.get() == txt_rpw.get():
        messagebox.showinfo(title="Sucess", message="Your account has been created!")       # success pop-up
        with open("database/users.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
            cont_line = f.readlines()
        save = str(len(cont_line)) + ";" + txt_fname.get() + ";" + txt_lname.get() + ";" + txt_email.get() + \
            ";" + txt_uppw.get() + ";" + "user" + ";" + "images/user.png" + ";" + "0000/00/00 --:--" + ";" + "False" + ";" + "False" + \
            ";" + "False" + ";" + "False" + ";" + "False" + ";" + "False" + "\n"        # variable that has the whole default information of the user 
        with open("database/users.csv", "a", encoding="UTF-8") as f:  # append the new data
            f.write(save)
        reset_sign_in()
    else:
        messagebox.showerror(title="Warning!", message="The passwords must be the same!")       # warning pop-up


def sign_in():  # sign in function
    global user_id
    sucess = False
    with open("database/users.csv", "r", encoding="UTF-8") as f:       # open the file to read and to compare the user id with the data
        for line in f:
            words = line.split(";")
            if txt_user.get() == words[3] and txt_pw.get() == words[4]:     # condition that confirms if the passwords are the same
                sucess = True
                user_id = words[0]
                window.destroy()
                menu.menu(user_id)
                break
        if sucess == False:
            messagebox.showerror(title="Warning!", message="The password or email doesn't exist or are incorrect!")     # error pop-up
            reset_sign_in()


window = function.tk_window("MOVIETIME", "900x650", [1000, 650], [1000, 650])  # Main Window
window.configure(background="#E0ECE4")

user_id = 0
# region Sign in
frame1 = function.place_label_frame(window, text="Welcome back!", width=350, height=550, x=600, y=50)

lbl_user = function.place_label(frame1, "Email", 150, 50)
txt_user = function.place_entry(frame1, 30, 80, 75)

lbl_pw = function.place_label(frame1, "Password", 140, 120)
txt_pw = function.place_entry(frame1, 30, 80, 145, "*")

btn1 = function.place_button(frame1, "Sign In", "white", sign_in, 120, 200)
# endregion

# region Sign Up
frame2 = function.place_label_frame(window, "New Account", 500, 550, 50, 50)

lbl_fname = function.place_label(frame2, "First Name", 220, 50)
txt_fname = function.place_entry(frame2, 30, 160, 75)

lbl_lname = function.place_label(frame2, "Last Name", 220, 120)
txt_lname = function.place_entry(frame2, 30, 160, 145)

lbl_email = function.place_label(frame2, "Email", 230, 190)
txt_email = function.place_entry(frame2, 30, 160, 215)

lbl_uppw = function.place_label(frame2, "Password", 220, 260)
txt_uppw = function.place_entry(frame2, 30, 160, 285, "*")

lbl_rpw = function.place_label(frame2, "Re-enter your Password", 190, 330)
txt_rpw = function.place_entry(frame2, 30, 160, 355, "*")

btn2 = function.place_button(frame2, "Sign Up", "white", sign_up, 200, 400)
# endregion

# region Reset
reset_btn2 = function.place_button(frame2, "Reset", "black", reset_sign_in, 270, 400)
reset_btn1 = function.place_button(frame1, "Reset", "black", reset_sign_up, 180, 200)
# endregion

# window
window.mainloop()
