from tkinter import LabelFrame, Misc, Entry, Label, Button, ttk, Tk, PanedWindow
from typing import List

def place_label_frame(window: Misc, text: str, width: int, height: int, x: int, y: int, fg: str = "black") -> LabelFrame:
    label_frame = LabelFrame(
        window, text=text, width=width, height=height, fg=fg)
    label_frame.place(x=x, y=y)
    return label_frame


def place_label(window: Misc, text: str, x: int, y: int, fg: str = "black") -> Label:
    label = Label(window, text=text, fg=fg)
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


def tk_window(geometry: str, title: str, fullscreen: str = "") -> Tk:
    window = Tk()
    window.geometry(geometry)
    window.state(fullscreen)
    window.title(title)
    window.iconbitmap("popcorn_icon.ico")
    return window


def panel_window(window: Misc, width: int, height: int, x: int, y: int):
    panel = PanedWindow(window, width = width, height = height, bd = "3", relief = "sunken")
    panel.place(x=x,y=y)
    return panel
