import tkinter as tk
from Config.Configuration import Configuration  # Importe la classe Configuration depuis le module Config.Configuration
from IHM.StrategyPaint import StrategyPaint  # Importe la classe StrategyPaint depuis le module IHM.StrategyPaint
from Algo.manager import Manager  # Importe la classe Manager depuis le module Algo.manager
from IHM.victory import victory  # Importe la fonction victory depuis le module IHM.victory
from Algo.Negamax_for_game import Negamax  # Importe la classe Negamax depuis le module Algo.Negamax_for_game
from Algo.Position import Position  # Importe la classe Position depuis le module Algo.Position
from PIL import Image, ImageTk  # Importe les modules PIL pour la manipulation d'images

class Main:
    def __init__(self):
        # Initialisation de l'instance du Manager et de la StrategyPaint
        self.manager = Manager()  # Instance du Manager pour gérer la logique du jeu
        self.strategy_paint = StrategyPaint(self.manager)  # Instance de StrategyPaint pour dessiner le plateau de jeu
        self.active = True  # Variable pour indiquer si le jeu est en cours ou non
        self.blc = True  # Variable pour bloquer les clics pendant le tour de l'IA
        self.canvas = None  # Instance du canvas
        self.root = tk.Tk()  # Instance de la fenêtre principale
        self.manager.add_callback(self.on_fin_changed)  # Ajoute le callback pour la gestion de la fin de partie

    # Méthode callback pour la gestion de la fin de partie
    def on_fin_changed(self):
        if self.manager.get_fin() == 0:  # Si la partie continue
            self.strategy_paint.effacer_pions(self.canvas, self.manager.get_plato())  # Efface les pions du plateau
            self.active = True  # Indique que la partie est toujours active
        elif self.manager.get_fin() == 1:  # Si la partie est quittée
            self.root.destroy()  # Ferme la fenêtre principale

    # Méthode pour gérer les clics de souris sur le canvas
    def clic_souris(self, event, canvas):
        if self.blc:
            self.blc = False  # Bloque les clics pendant le tour de l'IA
            if not self.active:  # Si la partie est terminée
                return

            x, y = event.x, event.y  # Récupère les coordonnées du clic de souris
            ligne = y // Configuration.BLOCK_SIZE  # Calcule l'indice de ligne correspondant
            colonne = x // Configuration.BLOCK_SIZE  # Calcule l'indice de colonne correspondant

            if 0 <= ligne < self.manager.plato.get_line_count() and 0 <= colonne < self.manager.plato.get_column_count():
                if self.manager.play(colonne):  # Joue le coup si valide et vérifie s'il y a un gagnant
                    self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessine le pion sur le plateau
                    self.manager.prochainTour()  # Passe au prochain tour
                    canvas.update()
                    self.turnOfIA(canvas)  # Tour de l'IA
                else:
                    self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessine le pion sur le plateau
                    victory(self.manager.get_joueur_actuel().get_type(), self.manager)  # Affiche le message de victoire
                    self.active = False  # Indique que la partie est terminée
            else:
                print("Clic en dehors du plateau.")  # Message en cas de clic en dehors du plateau
            self.blc = True  # Débloque les clics après le tour de l'IA

    # Méthode pour le tour de l'IA
    def turnOfIA(self, canvas):
        coup_joue = self.manager.get_board()  # Récupère les coups joués
        pos = Position()  # Crée une instance de Position
        pos.initBoard(coup_joue)  # Initialise le plateau avec les coups joués
        negamax = Negamax()  # Crée une instance de Negamax
        valeur, col = negamax.solve(pos)  # Résout la position actuelle avec Negamax
        if self.manager.play(col):  # Joue le coup si valide et vérifie s'il y a un gagnant
            self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessine le pion sur le plateau
            self.manager.prochainTour()  # Passe au prochain tour
        else:
            self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessine le pion sur le plateau
            victory(self.manager.get_joueur_actuel().get_type(), self.manager)  # Affiche le message de victoire
            self.active = False  # Indique que la partie est terminée

    # Méthode principale pour lancer l'application
    def main(self):
        self.root.title("Simple Game Board")  # Titre de la fenêtre
        self.root.attributes('-fullscreen', True)  # Affichage en mode plein écran
        self.root.configure(bg='ivory')  # Couleur de fond de la fenêtre
        cell_size = Configuration.BLOCK_SIZE  # Taille des cellules du plateau
        self.canvas = tk.Canvas(self.root, width=(self.manager.plato.get_column_count() + 1) * cell_size,
                                height=(self.manager.plato.get_line_count() + 1) * cell_size)  # Crée le canvas
        self.canvas.pack()  # Affiche le canvas
        self.strategy_paint.paint(self.canvas, self.manager.plato)  # Dessine le plateau sur le canvas
        self.canvas.bind("<Button-1>", lambda event: self.clic_souris(event, self.canvas))  # Bind le clic de souris
        self.root.mainloop()  # Lance la boucle principale de la fenêtre

# Crée une instance de la classe Main et lance l'application
if __name__ == "__main__":
    main = Main()
    main.main()
