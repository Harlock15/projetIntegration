

class Pion:
    def __init__(self, position, joueur):
        self.position = position
        self.joueur = joueur


    def get_position(self):
        return self.position


    def set_position(self, position):
        self.position = position

    
    def get_joueur(self):
        return self.joueur