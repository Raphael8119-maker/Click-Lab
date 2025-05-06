from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import time
import threading


fn = Tk()
fn.title("Calculatrice")
fn.geometry("1280x720")
fn.resizable(width=False, height=False)
fn.configure(bg = "light blue")


my_font = tkFont.Font(size= 20)


image = Image.open("fiole.png")
photo = ImageTk.PhotoImage(image)
 


canvas = Canvas(fn, width=214, height=259)
canvas.pack()




fiole = canvas.create_image(0,0, anchor=NW, image=photo, tags="fiole")
        
recherche = 0


def compte_click(event):
   global recherche
   x , y = event.x, event.y
   # renvoie la position de l'image sous la forme [x, y] :
   fiole_coords = canvas.coords("fiole")
   # détection du clic sur l'image :
   if x >= fiole_coords[0] and x <= fiole_coords[0] + image.size[0]:
       if y >= fiole_coords[1] and y <= fiole_coords[1] + image.size[1]:
           print("fiole cliquée !")
           print(x,y)
           recherche += 1
           texte.set("Nombre de recherches : " + str(recherche))




   
# Création d'un widget Label (texte 'Résultat -> x')
texte = StringVar()
texte.set("Nombre de recherche : " + str(recherche))
labelResultat = Label(fn, text = "Nombre de clicks :", textvariable = texte, fg ='black', bg ='white').place(x=100, y=0)
 
Button(fn,text="Lootbox",font = my_font,command=fn.destroy).place(x=100,y=400)
Button(fn,text="Lootbox",font = my_font,command=fn.destroy).place(x=1000,y=400)




canvas.bind("<Button-1>",compte_click)
fn.mainloop()
