from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Rng

def lancer_main(recherche = 0):
    """
    
    Lance l'interface graphique principale du jeu.
    
    """

    # Création de la fenêtre principale
    fn = Tk()
    fn.title("Calculatrice")
    fn.geometry("1280x720")
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")

    # Police pour les boutons
    my_font = tkFont.Font(size=20)

    # Chargement de l'image de la fiole
    image = Image.open("fiole.png")
    photo = ImageTk.PhotoImage(image)

    # Création du canvas et ajout de l'image
    canvas = Canvas(fn, width=214, height=259)
    canvas.pack()
    fiole = canvas.create_image(0, 0, anchor=NW, image=photo, tags="fiole")

    # Initialisation du compteur de clics
    texte = StringVar()
    texte.set("Nombre de recherche : " + str(recherche))

    def compte_click(event):
        """
        
        Gère les clics de souris sur le canvas.
        Si le clic est dans les limites de l'image, incrémente le compteur.
        
        """
        nonlocal recherche
        x, y = event.x, event.y
        fiole_coords = canvas.coords("fiole")
        if x >= fiole_coords[0] and x <= fiole_coords[0] + image.size[0]:
            if y >= fiole_coords[1] and y <= fiole_coords[1] + image.size[1]:
                recherche += 1
                texte.set("Nombre de recherches : " + str(recherche))

    # Définition de listes de compétences et lootboxes
    competencesLootBoxRare = ["competence1", "competence2", "competence3"]
    lootboxes = ["LootBox Rare"]

    def ouvrir_lootbox():
        """
        
        Ferme la fenêtre actuelle et ouvre l'interface de lootbox via le module Rng.
        
        """
        fn.destroy()
        Rng.lancer_lootbox_interface(recherche, competencesLootBoxRare, lootboxes)

    # Affichage du compteur de clics
    Label(fn, text="Nombre de clicks :", textvariable=texte, fg='black', bg='white').place(x=100, y=0)

    # Bouton pour ouvrir une lootbox
    Button(fn, text="LootBox", font=my_font, command=ouvrir_lootbox).place(x=100, y=400)

    # Bouton pour ouvrir l'arbre des compétences
    Button(fn, text="Arbre des Compétences", font=my_font, command=fn.destroy).place(x=900, y=400)

    # Lier le clic de souris à la fonction de comptage
    canvas.bind("<Button-1>", compte_click)
    
    fn.mainloop()

# Lancement initial
if __name__ == "__main__":
    lancer_main()
    