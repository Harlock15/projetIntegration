from tkinter import *

from IHM.StrategyPaint import StrategyPaint
from Algo.manager import Manager

class victory(Toplevel):
    def __init__(self, gagnant,manager):
        super().__init__()
        self.title("Vainqueur")
        self.geometry("400x200")  # Définir la taille de la fenêtre de victoire
        self.manager = manager
        # Étiquette pour afficher le gagnant
        self.label = Label(self, text="Le gagnant est le joueur " + gagnant, font=("Arial", 16))
        self.label.pack(pady=20)

        # Boutons pour commencer et quitter
        self.btn1 = Button(self, text="Continuer", font=("Arial", 12), padx=10, pady=5, command=self.continuer)
        self.btn2 = Button(self, text="Quitter", font=("Arial", 12), padx=10, pady=5, command=self.quitter)
        self.btn1.pack(side=LEFT, padx=20)
        self.btn2.pack(side=LEFT, padx=20)

    def continuer(self):
        self.manager.set_fin(0)
        self.destroy()

    def quitter(self):
        self.manager.set_fin(1)





