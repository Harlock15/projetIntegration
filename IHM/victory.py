from tkinter import *

from IHM.StrategyPaint import StrategyPaint  # Importe la classe StrategyPaint depuis le module IHM.StrategyPaint
from Algo.manager import Manager  # Importe la classe Manager depuis le module Algo.manager

class victory(Toplevel):
    def __init__(self, gagnant, manager):
        super().__init__()
        self.title("Vainqueur")  # Définit le titre de la fenêtre de victoire
        self.geometry("400x200")  # Définit la taille de la fenêtre de victoire
        self.manager = manager  # Référence vers l'instance du gestionnaire de jeu

        # Étiquette pour afficher le gagnant
        self.label = Label(self, text="Le gagnant est le joueur " + gagnant, font=("Arial", 16))
        self.label.pack(pady=20)

        # Boutons pour continuer ou quitter
        self.btn1 = Button(self, text="Continuer", font=("Arial", 12), padx=10, pady=5, command=self.continuer)
        self.btn2 = Button(self, text="Quitter", font=("Arial", 12), padx=10, pady=5, command=self.quitter)
        self.btn1.pack(side=LEFT, padx=20)
        self.btn2.pack(side=LEFT, padx=20)

    def continuer(self):
        # Appelle la méthode set_fin du gestionnaire de jeu avec la valeur 0 (continuer)
        self.manager.set_fin(0)
        self.destroy()  # Ferme la fenêtre de victoire

    def quitter(self):
        # Appelle la méthode set_fin du gestionnaire de jeu avec la valeur 1 (quitter)
        self.manager.set_fin(1)
