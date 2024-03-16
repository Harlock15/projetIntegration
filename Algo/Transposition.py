class Transposition:
    def __init__(self):
        self.dict = {}

    def put(self, key, value):
        self.dict[key] = value

    def get(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        return None
