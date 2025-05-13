from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Rng
import Main

fn = Tk()
fn.title("Main - ClickLab")
fn.geometry("1280x720")
fn.resizable(width=False, height=False)
fn.configure(bg="light blue")

my_font = tkFont.Font(size = 20)

Button(fn, text="Jouer", font=my_font, command=lambda: Main.lancer_main()).place(x=0, y=0)
fn.mainloop()