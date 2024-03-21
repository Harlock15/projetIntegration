# builder.py

from Data.Plateau import Plateau
from Data.Joueur import Joueur
from Config.Configuration import Configuration

class Builder:
    @staticmethod
    def init_plato():
        return Plateau(Configuration.LINE_COUNT, Configuration.COLUMN_COUNT)

    @staticmethod
    def init_joueur(type):
        return Joueur(type)