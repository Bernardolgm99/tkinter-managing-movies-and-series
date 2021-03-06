from tkinter import (Button, Entry, Label, LabelFrame, Listbox, Misc, PanedWindow, PhotoImage, Text, Tk, Toplevel, ttk)
from tkinter.constants import SUNKEN
from typing import List

from PIL import Image, ImageTk


def place_img(window: Misc, img: str) -> ImageTk.PhotoImage:    # place image function
    img_movie = Image.open(img)
    resized = img_movie.resize((338,500), Image.ANTIALIAS)
    img_movie_resized = ImageTk.PhotoImage(resized, master=window)
    return img_movie_resized


def place_text(window: Misc, width: int, height: int, x: int, y: int, fg: str = "black", font: str = "Verdana"): # place text function
    txt = Text(window, width=width, height=height, fg=fg, font=font, wrap="word",relief="flat")
    txt.place(x=x,y=y)
    return txt


def place_label_frame(window: Misc, text: str, width: int, height: int, x: int, y: int, fg: str = "black") -> LabelFrame: # place label frame function
    label_frame = LabelFrame(
        window, text=text, width=width, height=height, fg=fg)
    label_frame.place(x=x, y=y)
    label_frame.configure(background="#E0ECE4")
    return label_frame


def place_label(window: Misc, text: str, x: int, y: int, fg: str = "black", font: str = None) -> Label: # place label function
    label = Label(window, text=text, fg=fg) if (font is None) else Label(window, text=text, fg=fg, font=font)
    label.place(x=x, y=y)
    label.configure(background="#E0ECE4")
    return label


def place_entry(window: Misc, width: int, x: int, y: int, show: str = "") -> Entry: # place entry function
    entry = Entry(window, width=width, show=show)
    entry.place(x=x, y=y)
    return entry


def place_button(window: Misc, text: str, fg: str, command, x: int, y: int) -> Button: # place button function
    button = Button(window, text=text, fg=fg, command=command, background="#797A7E")
    button.place(x=x, y=y)
    return button

def button_img(window: Misc, image: ImageTk.PhotoImage, command, width: int, height: int, x: int, y: int) -> Button: # place button image function
    button = Button(window, image=image, command=command, width = width, height = height)
    button.place(x=x, y=y)
    button.image = image
    return button


def catalog_view(panel: Misc, columns: List[str], columns_size: List[int], x: int = 0, y: int = 0): # place catalog view function
    tree = ttk.Treeview(panel, selectmode="browse",
                        columns=columns, show="headings")
    for i in range(len(columns)):
        tree.column(columns[i], width=columns_size[i], anchor="center")
        tree.heading(columns[i], text=columns[i])
    tree.place(x=x, y=y)
    return tree

def disable_event(): 
   pass

def tk_window(title: str, geometry: str = "1000x650",  min_size: List[int] = [0, 0], max_size: List[int] = [0, 0], fullscreen: str = "normal") -> Tk: # create window function
    window = Tk()
    window.geometry(geometry)
    window.minsize(width=min_size[0], height=min_size[1])
    window.maxsize(width=max_size[0], height=max_size[1])
    window.state(fullscreen)
    window.title(title)
    window.iconbitmap("popcorn_icon.ico")
    window.protocol("WM_DELETE_WINDOW", disable_event)
    return window


def toplevel_window(title: str, geometry: str = "1000x650",  min_size: List[int] = [0, 0], max_size: List[int] = [0, 0], fullscreen: str = "normal") -> Toplevel: # place top level function
    window = Toplevel()
    window.geometry(geometry)
    window.minsize(width=min_size[0], height=min_size[1])
    window.maxsize(width=max_size[0], height=max_size[1])
    window.state(fullscreen)
    window.title(title)
    window.iconbitmap("popcorn_icon.ico")
    return window


def panel_window(window: Misc, width: int, height: int, x: int, y: int): # place panel window function
    panel = PanedWindow(window, width=width, height=height, bd="3", relief="sunken")
    panel.place(x=x, y=y)
    return panel

def listbox_panel(window: Misc, width: int, height: int, x: int, y: int, selectmode: str = "multiple") -> Listbox: # place listbox function
    listbox = Listbox(window, width = width, height = height, selectmode=selectmode)
    listbox.place (x=x,y=y)
    return listbox
