from tkinter import *
from tkinter import ttk

def play_game():
    screen = Tk()
    screen.title('Крестики-Нолики')
    screen.geometry("500x500")
    style = ttk.Style()

    style.theme_use('clam')
    game_area = PhotoImage(file="./area.png")
    label = ttk.Label(image=game_area)
    label.pack()
