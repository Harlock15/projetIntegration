import tkinter as tk  # Importation du module tkinter pour l'interface graphique

from Algo.Negamax_for_game import Negamax
from Algo.Position import Position
from Config.Configuration import Configuration  # Importation de la classe Configuration depuis le module Config.Configuration
from PIL import Image, ImageTk  # Importation de modules PIL pour la manipulation d'images
from IHM.StrategyPaint import StrategyPaint  # Importation de la classe StrategyPaint depuis le module IHM.StrategyPaint
from Algo.manager import Manager  # Importation de la classe Manager depuis le module Algo.manager
from IHM.victory import victory  # Importation de la fonction victory depuis le module IHM.victory

class Main:
    def __init__(self):
        # Initialisation de l'instance du Manager et de la StrategyPaint
        self.manager = Manager()  # Instance du Manager pour gérer la logique du jeu
        self.strategy_paint = StrategyPaint(self.manager)  # Instance de StrategyPaint pour dessiner le plateau de jeu
        self.active = True  # Variable pour indiquer si le jeu est en cours ou non
        self.blc = True
        self.canvas=None
        self.root = tk.Tk()
        self.manager.add_callback(self.on_fin_changed)

    def on_fin_changed(self):
        if self.manager.get_fin() == 0:
            self.strategy_paint.effacer_pions(self.canvas, self.manager.get_plato())
            self.active = True
        elif self.manager.get_fin() == 1:
            self.root.destroy()



    # Méthode pour gérer les clics de souris sur le canvas
    def clic_souris(self, event, canvas):

        if self.blc :
            self.blc = False
            # Vérification si c'est le tour du joueur X
            if not self.active:  # Vérification si le jeu est toujours en cours
                return

            # Récupération des coordonnées du clic de souris
            x, y = event.x, event.y

            # Conversion des coordonnées en indice de ligne et de colonne sur le plateau
            ligne = y // Configuration.BLOCK_SIZE
            colonne = x // Configuration.BLOCK_SIZE

            print(colonne)
            # Vérification si les coordonnées se trouvent dans les limites du plateau
            if 0 <= ligne < self.manager.plato.get_line_count() and 0 <= colonne < self.manager.plato.get_column_count():
                if self.manager.play(colonne):  # Vérification si le coup est valide et s'il y a un gagnant
                    self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessin du pion sur le plateau
                    self.manager.prochainTour()  # Passage au prochain tour
                else:
                    self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessin du pion sur le plateau
                    victory(self.manager.get_joueur_actuel().get_type())  # Affichage du message de victoire
                    self.active = False  # Indiquer que le jeu est terminé

            else:
                print("Clic en dehors du plateau.")  # Message en cas de clic en dehors du plateau

            canvas.update()
            self.turnOfIA(canvas)

    def turnOfIA(self, canvas):
        coup_joue = self.manager.get_board()
        pos = Position()
        print(coup_joue)
        pos.initBoard(coup_joue)
        negamax = Negamax()
        valeur, col = negamax.solve(pos)
        print(valeur, col)
        if self.manager.play(col):  # Vérification si le coup est valide et s'il y a un gagnant
            self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessin du pion sur le plateau
            self.manager.prochainTour()  # Passage au prochain tour
        else:
            self.strategy_paint.paintP(self.manager.get_case(), canvas)  # Dessin du pion sur le plateau
            victory(self.manager.get_joueur_actuel().get_type())  # Affichage du message de victoire
            self.active = False  # Indiquer que le jeu est terminé
        self.blc = True

    # Méthode principale pour lancer l'application
    def main(self):
        root.title("Simple Game Board")  # Titre de la fenêtre
        root.attributes('-fullscreen', True)  # Affichage en mode plein écran

        root.configure(bg='ivory')  # Couleur de fond de la fenêtre

        cell_size = Configuration.BLOCK_SIZE  # Taille des cellules du plateau

        self.canvas = tk.Canvas(self.root, width=(self.manager.plato.get_column_count()+1) * cell_size,
                           height=(self.manager.plato.get_line_count()+1) * cell_size)

        self.canvas.pack()

        self.strategy_paint.paint(self.canvas, self.manager.plato)


        self.canvas.bind("<Button-1>", lambda event: self.clic_souris(event, self.canvas))

        self.root.mainloop()


