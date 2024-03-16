class Joueur:


    def __init__(self, type):
        self.type = type
        self.pions = []


    def get_type(self):
        return self.type


    def get_pions(self):
        return self.pions