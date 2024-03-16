class Case:
    def __init__(self, colonne, ligne):
        self.colonne = colonne
        self.ligne = ligne
        self.pion = None

    def get_colonne(self):
        return self.colonne

    def get_ligne(self):
        return self.ligne

    def get_pion(self):
        return self.pion
    def set_pion(self,p):
        self.pion=p
    def estVide(self):
        return self.pion is None
