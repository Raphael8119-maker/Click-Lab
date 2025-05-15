import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Main

def menu(recherche_initial = 0,fn = None):
    """
    
    Lance l'interface graphique du menu.
    
    """
    recherche = recherche_initial

    if fn is None :
        fn = tk.Tk()
        fn_bonne = True
    else :
        for widget in fn.winfo_children():
            widget.destroy()
        fn_bonne = False

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
    
    Button(fn, text="Quitter", font=my_font, command=fn.destroy).place(x=0, y=50)
    
    if fn_bonne :
        fn.mainloop()
    
if __name__ == "__main__":
    menu()