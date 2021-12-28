from tkinter import *
from tkinter import messagebox

class app():
    def __init__(self):    #Sign In/Sin Up Menu 
        self.window = Tk()       #Main Window
        self.window.geometry("1000x800")
        self.window.title("WEBFLIX")

        #Sign In

        frame1 = LabelFrame(self.window, text="Sign In", width=350, height=200)
        frame1.place(x=470, y=450)

        lbl_user = Label(self.window, text="Email:", fg="black")      
        lbl_user.place(x=500, y=500)
        self.txt_user = Entry(self.window, width="30")
        self.txt_user.place(x=560, y=500)

        lbl_pw = Label(self.window, text="Password:", fg="black")
        lbl_pw.place(x=500, y=540)
        self.txt_pw = Entry(self.window, width="30", show="*")
        self.txt_pw.place(x=560, y=540)

        btn1 = Button(self.window, text="Sign In", fg="blue", command=self.sign_in)
        btn1.place(x=600, y=600)

        #Sign Up

        frame2 = LabelFrame(self.window, text="Sign Up", width=365, height=300)
        frame2.place(x=100, y=350)

        lbl_fname = Label(self.window, text="First Name:", fg="black")
        lbl_fname.place(x=125, y=400)
        self.txt_fname = Entry(self.window, width="12")
        self.txt_fname.place(x=195, y=400)

        lbl_lname = Label(self.window, text="Last Name:", fg="black")
        lbl_lname.place(x=280, y=400)
        self.txt_lname = Entry(self.window, width="12")
        self.txt_lname.place(x=350, y=400)

        lbl_email = Label(self.window, text="Email:", fg="black")
        lbl_email.place(x=125, y=450)
        self.txt_email = Entry(self.window, width="43")
        self.txt_email.place(x=165, y=450)

        lbl_uppw = Label(self.window, text="Password:", fg="black")
        lbl_uppw.place(x=125, y=500)
        self.txt_uppw = Entry(self.window, width="40", show="*")
        self.txt_uppw.place(x=185, y=500)

        lbl_rpw = Label(self.window, text="Re-enter your Password:", fg="black")
        lbl_rpw.place(x=125, y=550)
        self.txt_rpw = Entry(self.window, width="27", show="*")
        self.txt_rpw.place(x=260, y=550)

        btn2 = Button(self.window, text="Sign Up", fg="blue", command=self.sign_up)
        btn2.place(x=290, y=600)

        #Reset

        reset_btn2 = Button(self.window, text="Reset", fg="red", command=self.reset_sign_in)
        reset_btn2.place(x=350, y=600)
        reset_btn1 = Button(self.window, text="Reset", fg="red", command=self.reset_sign_up)
        reset_btn1.place(x=650, y=600)

        #window
        self.window.mainloop()   

    def reset_sign_up(self):    #reset function of Sign Up
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_uppw.delete(0, END)
        self.txt_rpw.delete(0, END)

    def reset_sign_in(self):    #reset function of Sign In 
        self.txt_pw.delete(0, END)
        self.txt_user.delete(0, END)

    def sign_up(self):      #sign up function
        if self.txt_uppw.get() == self.txt_rpw.get():
            messagebox.showinfo(title="Sucess", message="Your account has been created!")
            save = self.txt_fname.get() + self.txt_lname.get() + ";" + self.txt_email.get() + ";" + self.txt_uppw.get() + ";" + "user" + "\n"
            f = open("utilizadores.txt", "a", encoding="UTF-8")                #append the new data
            f.write(save)       
            f.close()
            self.reset_sign_up()
        else:
            messagebox.showerror(title="Warning!", message="The passwords must be the same!")

    def sign_in(self):      #sign in function
        sucess = False
        f = open("utilizadores.txt", "r", encoding="UTF-8")
        for line in f:
            words = line.split(";")
            if self.txt_user.get() == words[1] and self.txt_pw.get() == words[2]:
                sucess=True
                f.close()
                self.window.withdraw()     #a tela não fica escondida, não funciona
                self.menu()       
        if sucess == False:
            messagebox.showerror(title="Warning!", message="The password or email doesn't exist or are incorrect!")
            self.reset_sign_in()

    def perfil(self):
        perfil_window = Tk()
        perfil_window.geometry("400x600")
        perfil_window.title("Perfil")

    def menu(self):
        new_window = Tk()
        new_window.geometry("1000x800")
        new_window.title("WEBFLIX")

        Menu_bar = Menu(new_window)

        Menu_bar.add_command(label="User Perfil", command=self.perfil)
        Menu_bar.add_command(label="Quit", command = quit)

        new_window.configure(menu=Menu_bar)

    def __init__(self):    #Sign In/Sin Up Menu 
        window = Tk()       #Main Window
        window.geometry("1000x800")
        window.title("WEBFLIX")

        #Sign In

        frame1 = LabelFrame(window, text="Sign In", width=350, height=200)
        frame1.place(x=470, y=450)

        lbl_user = Label(window, text="Email:", fg="black")      
        lbl_user.place(x=500, y=500)
        self.txt_user = Entry(window, width="30")
        self.txt_user.place(x=560, y=500)

        lbl_pw = Label(window, text="Password:", fg="black")
        lbl_pw.place(x=500, y=540)
        self.txt_pw = Entry(window, width="30", show="*")
        self.txt_pw.place(x=560, y=540)

        btn1 = Button(window, text="Sign In", fg="blue", command=self.sign_in)
        btn1.place(x=600, y=600)

        #Sign Up

        frame2 = LabelFrame(window,  text="Sign Up", width=365, height=300)
        frame2.place(x=100, y=350)

        lbl_fname = Label(window, text="First Name:", fg="black")
        lbl_fname.place(x=125, y=400)
        self.txt_fname = Entry(window, width="12")
        self.txt_fname.place(x=195, y=400)

        lbl_lname = Label(window, text="Last Name:", fg="black")
        lbl_lname.place(x=280, y=400)
        self.txt_lname = Entry(window, width="12")
        self.txt_lname.place(x=350, y=400)

        lbl_email = Label(window, text="Email:", fg="black")
        lbl_email.place(x=125, y=450)
        self.txt_email = Entry(window, width="43")
        self.txt_email.place(x=165, y=450)

        lbl_uppw = Label(window, text="Password:", fg="black")
        lbl_uppw.place(x=125, y=500)
        self.txt_uppw = Entry(window, width="40", show="*")
        self.txt_uppw.place(x=185, y=500)

        lbl_rpw = Label(window, text="Re-enter your Password:", fg="black")
        lbl_rpw.place(x=125, y=550)
        self.txt_rpw = Entry(window, width="27", show="*")
        self.txt_rpw.place(x=260, y=550)

        btn2 = Button(window, text="Sign Up", fg="blue", command=self.sign_up)
        btn2.place(x=290, y=600)

        #Reset

        reset_btn2 = Button(window, text="Reset", fg="red", command=self.reset_sign_up)
        reset_btn2.place(x=350, y=600)
        reset_btn1 = Button(window, text="Reset", fg="red", command=self.reset_sign_in)
        reset_btn1.place(x=650, y=600)

        #window
        window.mainloop()   

app()