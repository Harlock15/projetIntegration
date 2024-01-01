from Data.Case import Case
class Plateau:
    def __init__(self, line_count, column_count):
        self.line_count = line_count
        self.column_count = column_count
        self.cases = [[Case(line_index, column_index) for column_index in range(column_count)] for line_index in
                      range(line_count)]

    def get_cases(self):
        return self.cases

    def get_line_count(self):
        return self.line_count

    def get_case(self, line, column):
        return self.cases[line][column]

    def get_column_count(self):
        return self.column_count

