from tkinter import *
from tkinter import messagebox

def perfil():
    perfil_window = Tk()
    perfil_window.geometry("400x600")
    perfil_window.title("Perfil")

    #window
    perfil_window.mainloop()

def menu():
    new_window = Tk()
    new_window.geometry("1000x800")
    new_window.state("zoomed")
    new_window.title("MOVIETIME")

    Menu_bar = Menu(new_window)

    Menu_bar.add_command(label="User Perfil", command=perfil)
    Menu_bar.add_command(label="Quit", command = quit)

    new_window.configure(menu=Menu_bar)
    
    #window
    new_window.mainloop()


