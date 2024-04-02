class Case:
    def __init__(self, colonne, ligne):
        """
        Constructeur de la classe Case.
        
        Args:
            colonne (int): La colonne de la case.
            ligne (int): La ligne de la case.
        """
        self.colonne = colonne
        self.ligne = ligne
        self.pion = None  # Initialisation de la case sans pion

    def get_colonne(self):
        """
        Renvoie la colonne de la case.
        """
        return self.colonne

    def get_ligne(self):
        """
        Renvoie la ligne de la case.
        """
        return self.ligne

    def get_pion(self):
        """
        Renvoie le pion actuellement dans la case.
        """
        return self.pion

    def set_pion(self, p):
        """
        Définit le pion dans la case.
        
        Args:
            p (object): Le pion à placer dans la case.
        """
        self.pion = p

    def estVide(self):
        """
        Vérifie si la case est vide.
        
        Returns:
            bool: True si la case est vide, False sinon.
        """
        return self.pion is None
