from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import function


def image():
    filename = filedialog.askopenfilename(title="Select file", filetypes=(("jpg files", ".jpg"), ("png files", ".png"),("jpeg files", ".jpeg"),("tiff files", ".tiff")))

def perfil():
    perfil_window = Tk()
    perfil_window.geometry("600x800")
    perfil_window.title("Perfil")
    perfil_window.iconbitmap("popcorn_icon.ico")

    perfil_window = Canvas(perfil_window, width=450, height=450)
    perfil_window.pack()
    img = PhotoImage(file="user.png")
    perfil_window.create_image(0,0, anchor = NW, image = img)

    #btn_avatar = function.place_button(perfil_window, "New Profile Pic", "blue", image, 0, 0)

def last_session():
    print()
    
def menu():
    new_window = Tk()
    new_window.geometry("1000x800")
    new_window.state("zoomed")
    new_window.minsize(width=1920 ,height=1080)
    new_window.maxsize(width=1920 ,height=1080)
    new_window.title("MOVIETIME")
    new_window.iconbitmap("popcorn_icon.ico")

    Menu_bar = Menu(new_window)

    Menu_bar.add_command(label="User Perfil", command=perfil)
    Menu_bar.add_command(label="Quit", command = last_session)

    new_window.configure(menu=Menu_bar)
    
    panel = PanedWindow(new_window, width= 450, height= 270, bd ="3", relief = "sunken")
    panel.place(x=0, y=0)
    tree = function.catalog_view(panel,("Nome","Email","Senha","Tipo"), (100,100,100,150)) #type: ignore

