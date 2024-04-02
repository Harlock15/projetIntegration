from Config import Configuration  # Import de la classe Configuration depuis le module Config

class StrategyPaint:
    def __init__(self, manager):
        """
        Constructeur de la classe StrategyPaint.
        
        Args:
            manager: Le gestionnaire du jeu.
        """
        self.manager = manager  # Gestionnaire du jeu
        self.cell_size = Configuration.Configuration.BLOCK_SIZE  # Taille d'une cellule du plateau

    def paint(self, canvas, plato):
        """
        Dessine le plateau de jeu sur le canevas.
        
        Args:
            canvas: Le canevas sur lequel dessiner.
            plato: Le plateau de jeu à dessiner.
        """
        rows = plato.get_line_count()
        columns = plato.get_column_count()

        for row in range(rows):
            for col in range(columns):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                canvas.create_rectangle(x1, y1, x2, y2)  # Dessine une case du plateau
        canvas.create_line(2, 0, 2, 600)  # Dessine une ligne sur le canevas

    def paintP(self, case, canvas):
        """
        Dessine un pion sur la case spécifiée du plateau.
        
        Args:
            case: La case sur laquelle dessiner le pion.
            canvas: Le canevas sur lequel dessiner.
        """
        colonne = case.get_colonne()
        ligne = case.get_ligne()

        joueur = self.manager.get_joueurActuel()
        couleur = "red" if joueur == self.manager.get_joueurX() else "yellow"

        canvas.create_oval(colonne * self.cell_size, ligne * self.cell_size, (colonne + 1) * self.cell_size,
                           (ligne + 1) * self.cell_size, fill=couleur, tags="pion")  # Dessine un pion sur le canevas

    def effacer_pions(self, canvas, plato):
        """
        Efface tous les pions du plateau sur le canevas.
        
        Args:
            canvas: Le canevas sur lequel dessiner.
            plato: Le plateau de jeu à nettoyer.
        """
        rows = plato.get_line_count()
        columns = plato.get_column_count()

        for row in range(rows):
            for col in range(columns):
                case = plato.get_case(col, row)
                if case.get_pion() is not None:
                    case.set_pion(None)  # Réinitialise les pions sur chaque case

        canvas.delete("pion")  # Efface tous les pions du canevas
