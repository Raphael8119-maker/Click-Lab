import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Main

def menu(recherche_initial = 0,fn = fn):
    """
    
    Lance l'interface graphique du menu.
    
    """
    recherche = recherche_initial

    if fn is None :
        fn = tk.Tk()
        own_window = True
    else :
        for widget in fn.winfo_children():
            widget.destroy()
        own_window = False
    
    
    
    fn.title("Menu - ClickLab")
    fn.geometry("1280x720")
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")
    
    my_font = tkFont.Font(size = 20)

    def jouer():
        """
        
        Ferme la fenêtre actuelle et ouvre l'interface du jeu via le module Main.
        
        """
        for widget in fn.winfo_children():
            widget.destroy()
        Main.lancer_main(recherche,fn)

    Button(fn, text="Jouer", font=my_font, command=jouer).place(x=0, y=0)
    if own_window :
        fn.mainloop()
    
if __name__ == "__main__":
    menu()