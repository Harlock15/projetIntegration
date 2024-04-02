class Pion:
    def __init__(self, position, joueur):
        """
        Constructeur de la classe Pion.
        
        Args:
            position (tuple): Position du pion sur le plateau (ligne, colonne).
            joueur (Joueur): Joueur à qui appartient le pion.
        """
        self.position = position  # Position du pion sur le plateau
        self.joueur = joueur  # Joueur à qui appartient le pion

    def get_position(self):
        """
        Renvoie la position actuelle du pion.
        
        Returns:
            tuple: Position du pion sur le plateau (ligne, colonne).
        """
        return self.position

    def set_position(self, position):
        """
        Définit la nouvelle position du pion.
        
        Args:
            position (tuple): Nouvelle position du pion sur le plateau (ligne, colonne).
        """
        self.position = position

    def get_joueur(self):
        """
        Renvoie le joueur à qui appartient le pion.
        
        Returns:
            Joueur: Joueur à qui appartient le pion.
        """
        return self.joueur
