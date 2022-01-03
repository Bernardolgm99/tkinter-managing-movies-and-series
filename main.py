from tkinter import *
from tkinter import messagebox
import function
import menu

def reset_sign_in():    #reset function of Sign Up
    txt_fname.delete(0, END)
    txt_lname.delete(0, END)
    txt_email.delete(0, END)
    txt_uppw.delete(0, END)
    txt_rpw.delete(0, END)

def reset_sign_up():    #reset function of Sign In 
    txt_pw.delete(0, END)
    txt_user.delete(0, END)


def sign_up():      #sign up function
    if txt_uppw.get() == txt_rpw.get():
        messagebox.showinfo(title="Sucess", message="Your account has been created!")
        save = txt_fname.get() + txt_lname.get() + ";" + txt_email.get() + ";" + txt_uppw.get() + ";" + "user" + "\n"
        with open("utilizadores.csv", "a", encoding="UTF-8") as f:                 #append the new data
            f.write(save)       
        reset_sign_up()
    else:
        messagebox.showerror(title="Warning!", message="The passwords must be the same!")

def sign_in():      #sign in function
    sucess = False
    with open("utilizadores.csv", "r", encoding="UTF-8") as f:
        for line in f:
            words = line.split(";")
            if txt_user.get() == words[1] and txt_pw.get() == words[2]:
                sucess=True
                window.withdraw()     #a tela não fica escondida, não funciona
                menu.menu()       
        if sucess == False:
            messagebox.showerror(title="Warning!", message="The password or email doesn't exist or are incorrect!")
            reset_sign_in()


window = Tk()       #Main Window
window.geometry("1000x800")
window.state("zoomed")
window.title("MOVIETIME")

#Sign in


frame1 = function.place_label_frame(window, text="Sign In", width=350, height=200, x=470, y=450)

lbl_user = function.place_label(window, "Email:", 500, 500)      
txt_user = function.place_entry(window, "30", 560, 500)

lbl_pw = function.place_label(window, "Password:", 500, 540 )
txt_pw = function.place_entry(window, "30", 560, 540, "*")

btn1 = function.place_button(window, "Sign In", "blue", sign_in, 600, 600)

#Sign Up

frame2 = function.place_label_frame(window, "Sign Up", 365, 300, 100, 350)

lbl_fname = function.place_label(window, "First Name:", 125, 400)
txt_fname = function.place_entry(window, "12", 195, 400)

lbl_lname = function.place_label(window, "Last Name:", 280, 400)
txt_lname = function.place_entry(window, "12", 350, 400)

lbl_email = function.place_label(window, "Email:", 125, 450)
txt_email = function.place_entry(window, "43", 165, 450)

lbl_uppw = function.place_label(window, "Password:", 125, 500)
txt_uppw = function.place_entry(window,"40", 185, 500, "*")

lbl_rpw = function.place_label(window, "Re-enter your Password:", 125, 550)
txt_rpw = function.place_entry(window, "27", 260, 550, "*")

btn2 = function.place_button(window, "Sign Up", "blue", sign_up, 290, 600)

#Reset

reset_btn2 = function.place_button(window, "Reset", "red", reset_sign_in, 350, 600)
reset_btn1 = function.place_button(window, "Reset", "red", reset_sign_up, 650, 600)


#window
window.mainloop()