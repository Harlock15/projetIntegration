from Data.Case import Case
class Plateau:
    def __init__(self, line_count, column_count):
        self.line_count = line_count-1
        self.column_count = column_count
        self.cases = [[Case(line_index, column_index) for column_index in range(column_count)] for line_index in
                      range(line_count)]

    def get_cases(self):
        return self.cases

    def get_line_count(self):
        return self.line_count

    def get_case(self, line, column):
        if 0 <= line < len(self.cases) and 0 <= column < len(self.cases[0]):
            return self.cases[line][column]
        else:
            # Si les indices sont invalides, renvoyer une valeur par défaut ou élever une exception
            return None

    def get_column_count(self):
        return self.column_count

