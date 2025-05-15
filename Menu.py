from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Main

def menu(recherche_initial = 0):
    """
    
    Lance l'interface graphique du menu.
    
    """
    
    recherche = recherche_initial

    fn = Tk()
    fn.title("Menu - ClickLab")
    fn.geometry("1280x720")
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")

    my_font = tkFont.Font(size = 20)

    def jouer():
        """
        
        Ferme la fenêtre actuelle et ouvre l'interface du jeu via le module Main.
        
        """
        fn.destroy()
        Main.lancer_main(recherche)

    Button(fn, text="Jouer", font=my_font, command=jouer).place(x=0, y=0)

    fn.mainloop()
    
if __name__ == "__main__":
    menu()