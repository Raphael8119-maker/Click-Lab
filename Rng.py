from tkinter import *
import random
import time
import tkinter.font as tkFont
from PIL import Image, ImageTk 
import Main

#Non variable
listeCompetenceLootBoxRare = ["competence1","competence2","competence3"]
listeLootBox = ["LootBox Rare"]

def lancer_lootbox_interface(recherche_initial, listeCompetenceLootBoxRare, listeLootBox):
    fn = Tk()
    fn.title('LootBox - ClickLab')
    fn.geometry('1280x720')
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")
    my_font = tkFont.Font(size=14)

    image = Image.open("ImgCoffreRare.png")
    photo = ImageTk.PhotoImage(image)

    canvas = Canvas(fn, width=photo.width(), height=photo.height())
    canvas.place(x=0, y=0)

    canvas.image = photo
    canvas.create_image(0, 0, anchor=NW, image=photo, tags="LootBox1")

    texte_depart = StringVar()
    texte_depart.set("Bienvenue dans le shop de competence. Veuillez choisir une lootbox !")
    labelDepart = Label(fn, textvariable=texte_depart, fg='Black', bg='light blue', font=my_font, width=120, height=3)
    labelDepart.place(x=0, y=580)

    texte_loot = StringVar()
    texte_loot.set("En attente du choix de la LootBox.")
    label_loot = Label(fn, textvariable=texte_loot, fg='Black', bg='light blue', font=my_font, width=120, height=3)
    label_loot.place(x=0, y=650)

    def retour():
        fn.destroy()
        Main.lancer_main()
    
    Button(fn, text="Retour", font=my_font, command=retour).place(x=0, y=560)
    
    recherche = recherche_initial

    def nouveau_lancer():
        nonlocal recherche
        nonlocal listeCompetenceLootBoxRare
        if recherche >= 100:
            if len(listeCompetenceLootBoxRare) != 0:
                competence_choisie = random.choice(listeCompetenceLootBoxRare)
                texte_loot.set(competence_choisie)
                listeCompetenceLootBoxRare.remove(competence_choisie)
                recherche -= 100
            else:
                texte_loot.set("Vous avez acheté toutes les compétences de cette LootBox")
        else:
            texte_loot.set("Pas assez de recherche, il vous en reste : " + str(recherche))

    def detec_clic(event):
        x, y = event.x, event.y
        LootBox1_coords = canvas.coords("LootBox1")
        if x >= LootBox1_coords[0] and x <= LootBox1_coords[0] + image.size[0]:
            if y >= LootBox1_coords[1] and y <= LootBox1_coords[1] + image.size[1]:
                texte_depart.set("Vous avez choisie la " + listeLootBox[0])
                nouveau_lancer()
                

    canvas.bind("<Button-1>", detec_clic)
    fn.mainloop()
