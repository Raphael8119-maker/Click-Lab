from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import Rng

def lancer_main():
    fn = Tk()
    fn.title("Calculatrice")
    fn.geometry("1280x720")
    fn.resizable(width=False, height=False)
    fn.configure(bg="light blue")

    my_font = tkFont.Font(size=20)
    image = Image.open("C:\\Users\\Utiliasteur\\OneDrive\\Documents\\visual studio\\fiole.png")
    photo = ImageTk.PhotoImage(image)

    canvas = Canvas(fn, width=214, height=259)
    canvas.pack()
    fiole = canvas.create_image(0, 0, anchor=NW, image=photo, tags="fiole")

    recherche = 0
    texte = StringVar()
    texte.set("Nombre de recherche : " + str(recherche))

    def compte_click(event):
        nonlocal recherche
        x, y = event.x, event.y
        fiole_coords = canvas.coords("fiole")
        if x >= fiole_coords[0] and x <= fiole_coords[0] + image.size[0]:
            if y >= fiole_coords[1] and y <= fiole_coords[1] + image.size[1]:
                recherche += 1
                texte.set("Nombre de recherches : " + str(recherche))

    competences = ["competence1", "competence2", "competence3"]
    lootboxes = ["LootBox Rare"]

    def ouvrir_lootbox():
        fn.destroy()
        Rng.lancer_lootbox_interface(recherche, lootboxes, competences)

    Label(fn, text="Nombre de clicks :", textvariable=texte, fg='black', bg='white').place(x=100, y=0)
    Button(fn, text="LootBox", font=my_font, command=ouvrir_lootbox).place(x=100, y=400)
    Button(fn, text="Arbre Des Compétences", font=my_font, command=fn.destroy).place(x=1000, y=400)

    canvas.bind("<Button-1>", compte_click)
    fn.mainloop()

# Lancement initial
if __name__ == "__main__":
    lancer_main()