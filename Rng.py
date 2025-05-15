from tkinter import *
import random
import tkinter.font as tkFont
from PIL import Image, ImageTk 
import Main


def lancer_lootbox_interface(recherche_initial, listeCompetenceLootBoxRare, listeLootBox, fn):
    """
    
    Lance l'interface graphique de la lootbox.
    
    """
    
    recherche = recherche_initial
    
    #Permet de savoir si une fenetre et dejà ouverte, si oui on nettoie l'ancienne et si non on en créer un nouvelle
    if fn is None:
        fn = Tk()
        fn_bonne = True
    else:
        fn_bonne = False
        for widget in fn.winfo_children():
            widget.destroy()
    
    # Changement de la fenêtre de jeu
    fn.title('LootBox - ClickLab')
    fn.geometry('1280x720')
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")
    
    # Taille des boutons
    my_font = tkFont.Font(size=14)
    my_font2 = tkFont.Font(size=10)
    
    # Chargement de l'image du coffre rare
    image = Image.open("ImgCoffreRare.png")
    photo = ImageTk.PhotoImage(image)

    # Création du canvas et ajout de l'image
    canvas = Canvas(fn, width=photo.width(), height=photo.height())
    canvas.place(x=5, y=0)
    canvas.image = photo
    canvas.create_image(0, 0, anchor=NW, image=photo, tags="LootBox1")

    # Création de texte d'acceuil / pour ce qui a été ouvert dans la lootbox
    texte_depart = StringVar()
    texte_depart.set("Bienvenue dans le shop de competence. Veuillez choisir une lootbox !")
    labelDepart = Label(fn, textvariable=texte_depart, fg='Black', bg='light blue', font=my_font, width=120, height=3)
    labelDepart.place(x=0, y=580)

    # Création de texte pour le choix des lootboxs
    texte_loot = StringVar()
    texte_loot.set("En attente du choix de la LootBox.")
    label_loot = Label(fn, textvariable=texte_loot, fg='Black', bg='light blue', font=my_font, width=120, height=3)
    label_loot.place(x=0, y=650)
    
    # Création d'un texte pour le prix
    textePrixLootboxRare = StringVar()
    textePrixLootboxRare.set("Le prix est de 50 recherches")
    labelPrixLootboxRare = Label(fn, textvariable=textePrixLootboxRare, fg='Black', bg='light blue', font=my_font2, width=20, height=3)
    labelPrixLootboxRare.place(x=5, y=150)
    
    def retour():
        """
        
        Ouvre l'interface du jeu via le module Main.
        
        """
        Main.lancer_main(recherche, fn)    

    def nouveau_lancer():
        '''
        
        Cette fonction permet faire un nouveau lancer de lootbox.
        
        '''
        nonlocal recherche
        nonlocal listeCompetenceLootBoxRare
        if recherche >= 50:
            if len(listeCompetenceLootBoxRare) != 0:
                competence_choisie = random.choice(listeCompetenceLootBoxRare)
                texte_loot.set(competence_choisie)
                listeCompetenceLootBoxRare.remove(competence_choisie)
                recherche -= 50
            else:
                texte_loot.set("Vous avez acheté toutes les compétences de cette LootBox")
        else:
            texte_loot.set("Pas assez de recherche, il vous en reste : " + str(recherche))

    def detec_clic(event):
        """
        
        Gère les clics de souris sur le canvas.
        Si le clic est dans les limites de l'image, ça choisi la bonne lootbox.
        
        """
        x, y = event.x, event.y
        LootBox1_coords = canvas.coords("LootBox1")
        if x >= LootBox1_coords[0] and x <= LootBox1_coords[0] + image.size[0]:
            if y >= LootBox1_coords[1] and y <= LootBox1_coords[1] + image.size[1]:
                texte_depart.set("Vous avez choisie la " + listeLootBox[0])
                nouveau_lancer()
                
    # Création d'un boutton pour revenir en arrière            
    Button(fn, text="Retour", font=my_font, command=retour).place(x=0, y=560)            

    # Lier le clic de souris à la fonction de comptage
    canvas.bind("<Button-1>", detec_clic)
    
    if fn_bonne :
        fn.mainloop()