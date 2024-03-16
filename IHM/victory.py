from tkinter import *


class victory(Toplevel):
    def __init__(self, gagnant):
        super().__init__()
        self.title("Vainqueur")
        self.geometry("400x200")  # Définir la taille de la fenêtre de victoire

        # Étiquette pour afficher le gagnant
        self.label = Label(self, text="Le gagnant est le joueur " + gagnant, font=("Arial", 16))
        self.label.pack(pady=20)

        # Boutons pour commencer et quitter
        self.btn1 = Button(self, text="Commencer", font=("Arial", 12), padx=10, pady=5, command=self.commencer)
        self.btn2 = Button(self, text="Quitter", font=("Arial", 12), padx=10, pady=5, command=self.quitter)
        self.btn1.pack(side=LEFT, padx=20)
        self.btn2.pack(side=LEFT, padx=20)

    def commencer(self):
        # Ajoutez ici le code pour commencer une nouvelle partie
        pass

    def quitter(self):
        self.destroy()


# Exemple d'utilisation de la classe Victory pour afficher une fenêtre de victoire
if __name__ == "__main__":
    # Simule la victoire d'un joueur, par exemple "Joueur 1"
    gagnant = "Joueur 1"

    # Crée une instance de la classe Victory avec le gagnant
    fenetre_victoire = victory(gagnant)
    fenetre_victoire.mainloop()
