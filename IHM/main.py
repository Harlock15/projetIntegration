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

    def clic_souris(self, event, canvas):
        x, y = event.x, event.y


        ligne = y // Configuration.BLOCK_SIZE
        colonne = x // Configuration.BLOCK_SIZE


        if 0 <= ligne < self.manager.plato.get_line_count() and 0 <= colonne < self.manager.plato.get_column_count():
            if self.manager.play(colonne) :
                self.strategy_paint.paintP(self.manager.get_case(), canvas)
                self.manager.prochainTour()
            else:
                self.strategy_paint.paintP(self.manager.get_case(), canvas)

                victory(self.manager.get_joueur_actuel().get_type())

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


        self.strategy_paint.paint(canvas, self.manager.plato)


        canvas.bind("<Button-1>", lambda event: self.clic_souris(event, canvas))

        root.mainloop()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
