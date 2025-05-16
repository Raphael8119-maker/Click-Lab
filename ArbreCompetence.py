from tkinter import *
from PIL import Image, ImageTk
import Rng
import Main
import tkinter.font as tkFont

competences = {
    "Compétence 1": 5,
    "Compétence 2": 10,
    "Compétence 3": 15,
    "Compétence 4": 20,
    "Compétence 5": 25,
    "Compétence 6": 30,
    "Compétence 7": 35,
    "Compétence 8": 40,
    "Compétence 9": 45,
    "Compétence 10": 50
}

def lancer_arbretechno_interface(recherche_initial, competencesLootBoxRare, lootboxes, fn) :
    
    recherche = recherche_initial
    
    #Permet de savoir si une fenetre et dejà ouverte, si oui on nettoie l'ancienne et si non on en créer un nouvelle
    if fn is None:
        fn = Tk()
        fn_bonne = True
    else:
        fn_bonne = False
        for widget in fn.winfo_children():
            widget.destroy()
    
    fn.title("Arbre des Compétences")
    fn.geometry("1280x720")
    fn.resizable(False, False)
    fn.configure(bg="lightblue")
    
    # Taille des boutons
    my_font = tkFont.Font(size=20)
        
    # Interface graphique
    texte = StringVar()
    texte.set("Arbre des Compétences")
    Label(fn, textvariable=texte, font=("Arial", 20), fg='black').place(x=500, y=10)

    Label(fn, text="Nombre de recherche :", font=("Arial", 14), bg="lightblue").place(x=50, y=200)
    valeur_recherche = StringVar()
    valeur_recherche.set(str(recherche))
    Label(fn, textvariable=valeur_recherche, font=("Arial", 14), bg="lightblue").place(x=250, y=200)

    texte_info = StringVar()
    texte_info.set("")
    Label(fn, textvariable=texte_info, font=("Arial", 14), fg="blue", bg="lightblue").place(x=50, y=240)

    # fonction pour acheter les compétences
    def acheter_competence(nom, cout):
        if recherche >= cout:
            recherche.set(recherche - cout)
            valeur_recherche.set(str(recherche))
            texte_info.set(nom + " débloquée !")
        else:
            texte_info.set("Pas assez de recherche pour " + nom)

    # boucle pour pouvoir créer les boutons de compétences automatiquement
    y = 300
    for nom, cout in competences.items():
        texte_bouton = nom + " (" + str(cout) + ")"
        Button(fn, text=texte_bouton, width=30, command=lambda n=nom, c=cout: acheter_competence(n, c)).place(x=50, y=y)
        y += 50
        
    def retour():
        """
        
        Ouvre l'interface du jeu via le module Main.
        
        """
        Main.lancer_main(recherche, fn) 
        
    Button(fn, text="retour", font=my_font, command=retour).place(x=1180, y=650)
    
    if fn_bonne :
        fn.mainloop()