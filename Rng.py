from tkinter import *
import random
import time
import tkinter.font as tkFont
from PIL import Image, ImageTk 

#Non variable
listeCompetenceLootBoxRare = ["competence1","competence2","competence3"]
listeLootBox = ["LootBox Rare"]

def nouveau_lancer():
    '''
    
    Cette fonction permet de générer un nouveau lancer aléatoire dans la liste des compétences
    
    ''' 
    global recherche
    if recherche >= 100 :
        if len(listeCompetenceLootBoxRare) != 0 :
            competence_choisie = random.choice(listeCompetenceLootBoxRare)
            texte_loot.set(competence_choisie)
            listeCompetenceLootBoxRare.remove(competence_choisie)
            recherche -= 100
        else :
            texte_loot.set("Vous avez acheté toutes les compétences de cette LootBox")
    else :
        texte_loot.set("Pas assez de recherche, il vous en reste : " + str(recherche))
        
def detec_clic(event):
    '''
    
    Cette fonction permet la detection de clic au niveau du canvas LootBox 1
    
    '''
    
    x , y = event.x, event.y
    
    # renvoie la position de l'image sous la forme [x, y] :
    LootBox1_coords = canvas.coords("LootBox1")
 
    # détection du clic sur l'image et si clic au bon endroit lance la def nouveau_lancer:
    if x >= LootBox1_coords[0] and x <= LootBox1_coords[0] + image.size[0]:
        if y >= LootBox1_coords[1] and y <= LootBox1_coords[1] + image.size[1]:
            lootBox_choisie(listeLootBox[0])
            nouveau_lancer()

def lootBox_choisie(rarete):
    
    '''
    
    Cette fonction permet de montrer quel LootBox a été choisie
    
    Paramètre :
    
    Rareté de la LootBox (Voir listeLootBox)
    
    '''
    
    texte_depart.set("Vous avez choisie la " + str(rarete))
 
 
def fnRng():    
# Création de la fenêtre principale (Main Window)
    fn = Tk()
    fn.title('LootBox - ClickLab')
    fn.geometry('1280x720')
    fn.resizable(width=False , height=False)
    fn.configure(bg= "light blue")
    my_font = tkFont.Font(size= 14)   

    image = Image.open('ImgCoffreRare.png')
    photo = ImageTk.PhotoImage(image)

    canvas = Canvas(fn, width=140, height=150)
    canvas.place(x= 0 ,y= 0)

    #Création de l'image LootBox1 avec le tags 'LootBox1' qui est utiliser dans la def detec_clic pour la commande canvas.coords()
    LootBox1 = canvas.create_image(0, 0, anchor=NW, image=photo, tags="LootBox1")

    #Texte en bas de l'écran avec les informations importantes + changement avec def nouveau_lancer
    texte_depart = StringVar()
    texte_depart.set("Bienvenue dans le shop de competence. Veuillez choisir une lootbox !")
    labelDepart = Label(fn, textvariable = texte_depart, fg ='Black', bg ='light blue',font= my_font, width= 120, height= 3)
    labelDepart.place(x= 0 , y= 580)

    #Deuxieme ligne de texte pour les loots des competences
    texte_loot = StringVar()
    texte_loot.set("En attente du choix de la LootBox.")
    label_loot = Label(fn, textvariable = texte_loot, fg ='Black', bg ='light blue',font= my_font, width= 120, height= 3)
    label_loot.place(x= 0 , y= 650)

    #Permet de savoir ou est le clic "<Button-1>" (clic gauche)
    canvas.bind("<Button-1>", detec_clic)      
