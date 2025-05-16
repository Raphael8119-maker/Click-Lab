from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Rng
import Menu
import ArbreCompetence

def lancer_main(recherche_initial, fn):
    """
    
    Lance l'interface graphique principale du jeu.
    
    """
    recherche = recherche_initial
    
    if fn is None:
        fn = Tk()
        fn_bonne = True
    else:
        fn_bonne = False
        # Nettoyer la fenêtre existante si besoin
        for widget in fn.winfo_children():
            widget.destroy()

    # Changement de la fenêtre de jeu
    fn.title("Main - ClickLab")
    fn.geometry("1280x720")
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")
    
    # Taille des boutons
    my_font = tkFont.Font(size=20)

    # Chargement de l'image de la fiole
    image = Image.open("fiole.png")
    photo = ImageTk.PhotoImage(image)

    # Création du canvas et ajout de l'image
    canvas = Canvas(fn, width=photo.width(), height=photo.height())
    canvas.place(x=550,y=0)
    canvas.image = photo
    canvas.create_image(0, 0, anchor=NW, image=photo, tags="fiole")

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
        
        Ouvre l'interface de lootbox via le module Rng.
        
        """
        Rng.lancer_lootbox_interface(recherche, competencesLootBoxRare, lootboxes, fn)
        
    def ouvrir_menu():
        """
        
        Ouvre l'interface du menu via le module Menu.
        
        """
        Menu.menu(recherche, fn) 
        
    def ouvrir_competence():
        """
        
        Ouvre l'interface du menu via le module Menu.
        
        """
        ArbreCompetence.lancer_arbretechno_interface(recherche, competencesLootBoxRare, lootboxes, fn)   

    # Affichage du compteur de clics
    Label(fn, text="Nombre de clicks :", textvariable=texte, fg='black', bg='light blue', font= my_font).place(x=100, y=0)

    # Bouton pour ouvrir une lootbox
    Button(fn, text="LootBox", font=my_font, command=ouvrir_lootbox).place(x=550, y=400)

    # Bouton pour ouvrir l'arbre des compétences
    Button(fn, text="Arbre des Compétences", font=my_font, command=ouvrir_competence).place(x=900, y=400)
    
    #Bouton pour retourner au menu principale 
    Button(fn, text="Menu Principal", font=my_font, command=ouvrir_menu).place(x=100, y=400)

    # Lier le clic de souris à la fonction de comptage
    canvas.bind("<Button-1>", compte_click)
    
    if fn_bonne :
        fn.mainloop()