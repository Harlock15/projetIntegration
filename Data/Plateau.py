from Data.Case import Case  # Import de la classe Case depuis le module Data.Case

class Plateau:
    def __init__(self, line_count, column_count):
        """
        Constructeur de la classe Plateau.
        
        Args:
            line_count (int): Nombre de lignes du plateau.
            column_count (int): Nombre de colonnes du plateau.
        """
        self.line_count = line_count - 1  # Nombre de lignes du plateau (indexé à partir de 0)
        self.column_count = column_count  # Nombre de colonnes du plateau
        # Création d'une liste 2D de cases en utilisant la classe Case
        self.cases = [[Case(line_index, column_index) for column_index in range(column_count)] for line_index in range(line_count)]

    def get_cases(self):
        """
        Renvoie toutes les cases du plateau.
        
        Returns:
            list: Liste des cases du plateau.
        """
        return self.cases

    def get_line_count(self):
        """
        Renvoie le nombre de lignes du plateau.
        
        Returns:
            int: Nombre de lignes du plateau.
        """
        return self.line_count

    def get_case(self, line, column):
        """
        Renvoie la case située à la ligne et la colonne spécifiées.
        
        Args:
            line (int): L'index de la ligne de la case.
            column (int): L'index de la colonne de la case.
        
        Returns:
            Case: La case située à la position spécifiée.
            None: Si les indices spécifiés sont hors des limites du plateau.
        """
        if 0 <= line < len(self.cases) and 0 <= column < len(self.cases[0]):
            return self.cases[line][column]
        else:
            return None

    def get_column_count(self):
        """
        Renvoie le nombre de colonnes du plateau.
        
        Returns:
            int: Nombre de colonnes du plateau.
        """
        return self.column_count
