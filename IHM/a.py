from tkinter import *
from PIL import Image, ImageTk

# Créer une fenêtre Tkinter
root = Tk()

# Créer un canevas
canvas = Canvas(root, width=1300, height=1200)
canvas.pack(expand=YES, fill=BOTH)

# Charger l'image JPEG
image = Image.open("image/bg1.png")

# Convertir l'image pour l'afficher avec Tkinter
photo = ImageTk.PhotoImage(image)

# Afficher l'image sur le canevas
canvas.create_image(0, 0, image=photo, anchor=NW)

# Lancer la boucle principale
root.mainloop()
