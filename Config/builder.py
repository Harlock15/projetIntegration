# builder.py

# Importation des classes nécessaires depuis d'autres modules
from Data.Plateau import Plateau
from Data.Joueur import Joueur
from Config.Configuration import Configuration

class Builder:
    @staticmethod
    def init_plato():
        """
        Méthode statique pour initialiser un plateau de jeu.
        
        Returns:
            Plateau: Instance de la classe Plateau avec le nombre de lignes et de colonnes spécifié par la configuration.
        """
        return Plateau(Configuration.LINE_COUNT, Configuration.COLUMN_COUNT)

    @staticmethod
    def init_joueur(type):
        """
        Méthode statique pour initialiser un joueur.
        
        Args:
            type (str): Le type du joueur à initialiser.
        
        Returns:
            Joueur: Instance de la classe Joueur avec le type spécifié.
        """
        return Joueur(type)
