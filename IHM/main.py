# main.py

import tkinter as tk
from Config.Configuration import Configuration
from Data.Case import Case
from IHM.StrategyPaint import StrategyPaint
from Algo.manager import Manager
from IHM.victory import victory


class Main:
    def __init__(self):
        self.manager = Manager()
        self.strategy_paint = StrategyPaint(self.manager)

    def clic_souris(self, event, canvas,root):
        x, y = event.x, event.y

        # Calculer la ligne et la colonne de la case correspondante aux coordonnées du clic
        ligne = y // Configuration.BLOCK_SIZE
        colonne = x // Configuration.BLOCK_SIZE

        # Vérifier si les coordonnées se trouvent dans les limites du plateau
        if 0 <= ligne < self.manager.plato.get_line_count() and 0 <= colonne < self.manager.plato.get_column_count():
            if self.manager.play(colonne) : # Appel de la méthode play pour ajouter un pion et vérifier la victoire
                self.strategy_paint.paintP(self.manager.get_case(), canvas)
                self.manager.prochainTour()
            else:
                self.strategy_paint.paintP(self.manager.get_case(), canvas)
                print(f"{self.manager.get_joueur_actuel().get_type()} à gagné")
                gagnant_window = victory(self.manager.get_joueur_actuel().get_type())

        else:
            print("Clic en dehors du plateau.")

    def main(self):
        root = tk.Tk()
        root.title("Simple Game Board")
        root.attributes('-fullscreen', True)

        cell_size = Configuration.BLOCK_SIZE
        canvas = tk.Canvas(root, width=(self.manager.plato.get_column_count()+1) * cell_size,
                           height=(self.manager.plato.get_line_count()+1) * cell_size)
        canvas.pack()

        # Créer une instance de StrategyPaint et appeler la méthode paint
        self.strategy_paint.paint(canvas, self.manager.plato)

        # Associer la fonction clic_souris à l'événement de clic de souris
        canvas.bind("<Button-1>", lambda event: self.clic_souris(event, canvas,root))

        root.mainloop()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
