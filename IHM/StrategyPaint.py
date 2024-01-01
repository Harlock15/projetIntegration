from Config import Configuration


class StrategyPaint:
    def __init__(self, manager):
        self.manager = manager
        self.cell_size = Configuration.Configuration.BLOCK_SIZE

    def paint(self, canvas, plato):
        rows = plato.get_line_count()
        columns = plato.get_column_count()


        for row in range(rows):
            for col in range(columns):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                canvas.create_rectangle(x1, y1, x2, y2)
        

    def paintP(self, case, canvas):
        colonne=case.get_colonne()
        ligne = case.get_ligne()

        # Ajouter la logique pour obtenir la couleur en fonction du joueur
        joueur = self.manager.get_joueurActuel()  # Supposons que votre méthode get_joueur retourne le numéro du joueur
        couleur = "red" if joueur == self.manager.get_joueurX() else "yellow"

        # Dessiner le pion sur la case spécifiée

        canvas.create_oval(colonne * self.cell_size, ligne * self.cell_size, (colonne + 1) * self.cell_size,
                           (ligne + 1) * self.cell_size, fill=couleur)


        

