from tkinter import *
from tkinter import messagebox


def f_reset1():    #reset function of Sign Up
    txt_fname.delete(0, END)
    txt_lname.delete(0, END)
    txt_email.delete(0, END)
    txt_uppw.delete(0, END)
    txt_rpw.delete(0, END)

def f_reset2():    #reset function of Sign In 
    txt_pw.delete(0, END)
    txt_user.delete(0, END)

def sign_up():      #sign up function
    if txt_uppw.get() == txt_rpw.get():
        messagebox.showinfo(title="Sucess", message="Your account has been created!")
        save = txt_fname.get() + txt_lname.get() + ";" + txt_email.get() + ";" + txt_uppw.get() + ";" + "user" + "\n"
        f = open("utilizadores.txt", "a", encoding="UTF-8")                #append the new data
        f.write(save)       
        f.close()
        f_reset1()
    else:
        messagebox.showerror(title="Warning!", message="The passwords must be the same!")

def sign_in():      #sign in function
    sucess = False
    f = open("utilizadores.txt", "r", encoding="UTF-8")
    for line in f:
        words = line.split(";")
        if txt_user.get() == words[1] and txt_pw.get() == words[2]:
            sucess=True
            f.close()
            window.destroy()
            menu()       
    if sucess == False:
        messagebox.showerror(title="Warning!", message="The password or email doesn't exist or are incorrect!")
        f_reset2()

def menu():
    new_window = Tk()
    new_window.geometry("1000x800")
    window.title("WEBFLIX")

#Sign In/Sin Up Menu 
window = Tk()       #Main Window
window.geometry("1000x800")
window.title("WEBFLIX")

#Sign In

frame1 = LabelFrame(window, text="Sign In", width=350, height=200)
frame1.place(x=470, y=450)

lbl_user = Label(window, text="Email:", fg="black")      
lbl_user.place(x=500, y=500)
txt_user = Entry(window, width="30")
txt_user.place(x=560, y=500)

lbl_pw = Label(window, text="Password:", fg="black")
lbl_pw.place(x=500, y=540)
txt_pw = Entry(window, width="30", show="*")
txt_pw.place(x=560, y=540)

btn1 = Button(window, text="Sign In", fg="blue", command=sign_in)
btn1.place(x=600, y=600)

#Sign Up

frame2 = LabelFrame(window,  text="Sign Up", width=365, height=300)
frame2.place(x=100, y=350)

lbl_fname = Label(window, text="First Name:", fg="black")
lbl_fname.place(x=125, y=400)
txt_fname = Entry(window, width="12")
txt_fname.place(x=195, y=400)

lbl_lname = Label(window, text="Last Name:", fg="black")
lbl_lname.place(x=280, y=400)
txt_lname = Entry(window, width="12")
txt_lname.place(x=350, y=400)

lbl_email = Label(window, text="Email:", fg="black")
lbl_email.place(x=125, y=450)
txt_email = Entry(window, width="43")
txt_email.place(x=165, y=450)

lbl_uppw = Label(window, text="Password:", fg="black")
lbl_uppw.place(x=125, y=500)
txt_uppw = Entry(window, width="40", show="*")
txt_uppw.place(x=185, y=500)

lbl_rpw = Label(window, text="Re-enter your Password:", fg="black")
lbl_rpw.place(x=125, y=550)
txt_rpw = Entry(window, width="27", show="*")
txt_rpw.place(x=260, y=550)

btn2 = Button(window, text="Sign Up", fg="blue", command=sign_up)
btn2.place(x=290, y=600)

#Reset

reset_btn2 = Button(window, text="Reset", fg="red", command=f_reset1)
reset_btn2.place(x=350, y=600)
reset_btn1 = Button(window, text="Reset", fg="red", command=f_reset2)
reset_btn1.place(x=650, y=600)

#window
window.mainloop()