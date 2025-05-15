from tkinter import *
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Arbre des Compétences")
fenetre.geometry("1280x800")
fenetre.resizable(False, False)
fenetre.configure(bg="lightblue")

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

nb_recherche = IntVar()
nb_recherche.set(150)


# Interface graphique
texte = StringVar()
texte.set("Arbre des Compétences")
Label(fenetre, textvariable=texte, font=("Arial", 20), fg='black').place(x=500, y=10)

image = Image.open("fiole.png")
image_logo = ImageTk.PhotoImage(image)
Label(fenetre, image=image_logo, bg="lightblue").place(x=560, y=50)

Label(fenetre, text="Nombre de recherche :", font=("Arial", 14), bg="lightblue").place(x=50, y=200)
valeur_recherche = StringVar()
valeur_recherche.set(str(nb_recherche.get()))
Label(fenetre, textvariable=valeur_recherche, font=("Arial", 14), bg="lightblue").place(x=250, y=200)

texte_info = StringVar()
texte_info.set("")
Label(fenetre, textvariable=texte_info, font=("Arial", 14), fg="blue", bg="lightblue").place(x=50, y=240)

# fonction pour acheter les compétences
def acheter_competence(nom, cout):
    actuel = nb_recherche.get()
    if actuel >= cout:
        nb_recherche.set(actuel - cout)
        valeur_recherche.set(str(nb_recherche.get()))
        texte_info.set(nom + " débloquée !")
        del competences(nom)
    else:
        texte_info.set("Pas assez de recherche pour " + nom)

y = 300
# boucle pour pouvoir créer les boutons de compétences automatiquement
for nom, cout in competences.items():
    texte_bouton = nom + " (" + str(cout) + ")"
    Button(fenetre, text=texte_bouton, width=30, command=lambda n=nom, c=cout: acheter_competence(n, c)).place(x=50, y=y)
    y += 50

fenetre.mainloop()