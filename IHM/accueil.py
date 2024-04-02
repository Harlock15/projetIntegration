import os
from tkinter import *
from PIL import Image, ImageTk
from IHM.StrategyPaint import StrategyPaint
from Algo.manager import Manager
from IHM.main import Main

class Accueil:
    def __init__(self):
        # Crée une instance de la fenêtre Tkinter en mode plein écran
        self.gui = Tk()
        self.gui.attributes('-fullscreen', True)

        # Initialise l'instance du Manager et de StrategyPaint
        self.manager = Manager()
        self.strategy_paint = StrategyPaint(self.manager)

        # Crée un canvas de la taille de l'écran
        canvas = Canvas(self.gui, width=self.gui.winfo_screenwidth(), height=self.gui.winfo_screenheight())
        canvas.pack(expand=YES, fill=BOTH)

        # Crée un label sur le canvas
        label = Label(canvas)
        label.pack(pady=150)

        # Charge l'image de fond depuis un fichier
        image = Image.open("image/bg1.png")

        # Convertit l'image pour l'afficher avec Tkinter
        photo = ImageTk.PhotoImage(image)

        # Affiche l'image sur le canevas
        canvas.create_image(0, 0, image=photo, anchor=NW)

        # Crée deux boutons sur le canevas pour commencer ou quitter le jeu
        self.btn1 = Button(canvas, text="Commencer", font=10, command=self.jeu, padx=32, pady=20)
        self.btn2 = Button(canvas, text="Quitter", font=10, command=self.gui.destroy, padx=32, pady=20)

        # Utilise la gestion de géométrie pack pour centrer les boutons
        self.btn1.pack(side=LEFT, padx=300)
        self.btn2.pack(side=LEFT, padx=100)

        # Lance la boucle principale de la fenêtre Tkinter
        self.gui.mainloop()

    def jeu(self):
        # Ferme la fenêtre d'accueil
        self.gui.destroy()

        # Crée une instance de la classe Main et lance le jeu
        main_instance = Main()
        main_instance.main()

# Lance l'application en créant une instance de la classe Accueil
if __name__ == "__main__":
    accueil = Accueil()
