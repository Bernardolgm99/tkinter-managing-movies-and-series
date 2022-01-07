from pathlib import Path
from tkinter import LabelFrame, Misc, Entry, Label, Button, Toplevel, ttk, Tk, PanedWindow, Text
from PIL import Image, ImageTk
from typing import List
from tkinter import *

#Não está sendo reconhecido o open do Image
def place_img(window: Misc, img: Path, side):
    img_movie = Image.open(img)
    resized = img_movie.resize((338,500), Image.ANTIALIAS)
    img_movie_resized = ImageTk.PhotoImage(resized)
    label_img_movie = Label(window, image=img_movie_resized, bd=5, relief=SUNKEN)
    label_img_movie.pack(padx=10, pady=10, side=side)
    return label_img_movie


def place_text(window: Misc, width: int, height: int, x: int, y: int, fg: str = "black", font: str = "Verdana"):
    txt = Text(window, width=width, height=height, fg=fg, font=font, wrap="word",relief="flat")
    txt.place(x=x,y=y)
    return txt


def place_label_frame(window: Misc, text: str, width: int, height: int, x: int, y: int, fg: str = "black") -> LabelFrame:
    label_frame = LabelFrame(
        window, text=text, width=width, height=height, fg=fg)
    label_frame.place(x=x, y=y)
    return label_frame


def place_label(window: Misc, text: str, x: int, y: int, fg: str = "black", font: str = "Verdana") -> Label:
    label = Label(window, text=text, fg=fg, font=font)
    label.place(x=x, y=y)
    return label


def place_entry(window: Misc, width: int, x: int, y: int, show: str = "") -> Entry:
    entry = Entry(window, width=width, show=show)
    entry.place(x=x, y=y)
    return entry


def place_button(window: Misc, text: str, fg: str, command, x: int, y: int) -> Button:
    button = Button(window, text=text, fg=fg, command=command)
    button.place(x=x, y=y)
    return button


def catalog_view(panel: Misc, columns: List[str], columns_size: List[int], x: int = 0, y: int = 0):
    tree = ttk.Treeview(panel, selectmode="browse",
                        columns=columns, show="headings")
    for i in range(len(columns)):
        tree.column(columns[i], width=columns_size[i], anchor="center")
        tree.heading(columns[i], text=columns[i])
    tree.place(x=x, y=y)
    return tree


def tk_window(title: str, geometry: str = "1000x650",  min_size: List[int] = [0, 0], max_size: List[int] = [0, 0], fullscreen: str = "normal") -> Tk:
    window = Tk()
    window.geometry(geometry)
    window.minsize(width=min_size[0], height=min_size[1])
    window.maxsize(width=max_size[0], height=max_size[1])
    window.state(fullscreen)
    window.title(title)
    window.iconbitmap("popcorn_icon.ico")
    return window


def toplevel_window(title: str, geometry: str = "1000x650",  min_size: List[int] = [0, 0], max_size: List[int] = [0, 0], fullscreen: str = "normal") -> Toplevel:
    window = Toplevel()
    window.geometry(geometry)
    window.minsize(width=min_size[0], height=min_size[1])
    window.maxsize(width=max_size[0], height=max_size[1])
    window.state(fullscreen)
    window.title(title)
    window.iconbitmap("popcorn_icon.ico")
    return window


def panel_window(window: Misc, width: int, height: int, x: int, y: int):
    panel = PanedWindow(window, width=width, height=height, bd="3", relief="sunken")
    panel.place(x=x, y=y)
    return panel
