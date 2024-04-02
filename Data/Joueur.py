class Joueur:
    def __init__(self, type):
        """
        Constructeur de la classe Joueur.
        
        Args:
            type (str): Le type de joueur (par exemple, "humain" ou "ia").
        """
        self.type = type  # Définition du type de joueur
        self.pions = []   # Initialisation de la liste des pions du joueur

    def get_type(self):
        """
        Renvoie le type de joueur.
        
        Returns:
            str: Le type de joueur.
        """
        return self.type

    def get_pions(self):
        """
        Renvoie la liste des pions du joueur.
        
        Returns:
            list: Liste des pions du joueur.
        """
        return self.pions
