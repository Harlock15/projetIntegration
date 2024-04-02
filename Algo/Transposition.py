class Transposition:
    """
    Classe pour la gestion de la table de transposition utilisée dans l'algorithme de Negamax.
    """
    def __init__(self):
        # Initialisation du dictionnaire pour stocker les entrées de la table de transposition
        self.dict = {}

    def put(self, key, value):
        """
        Méthode pour ajouter une entrée dans la table de transposition.
        
        Args:
            key: Clé de l'entrée à ajouter.
            value: Valeur associée à la clé.
        """
        self.dict[key] = value

    def get(self, key):
        """
        Méthode pour récupérer une valeur à partir de la table de transposition en utilisant la clé donnée.
        
        Args:
            key: Clé de l'entrée à récupérer.
        
        Returns:
            La valeur associée à la clé donnée, ou None si la clé n'est pas présente dans la table.
        """
        if key in self.dict.keys():
            return self.dict[key]
        return None
