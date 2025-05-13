from tkinter import *
from PIL import Image, ImageTk

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

image = Image.open("ImgCoffreRare.png")
photo = ImageTk.PhotoImage(image)

canvas.image = photo  # très important
canvas.create_image(0, 0, anchor=NW, image=photo)

root.mainloop()