
class Martix:
    def __init__(self,list):
        self.list = list
        self._row = len(list)
        self._col = len(list[0])

    def __str__(self):
        print("Матрица: ")
        for row in self.list:
            for i in row:
                print(f"{i}", end="\t")
            print()
        return ''

    def __add__(self, other):
        if self._row == other._row and self._col == other._col:
            for i in range(len(self.list)):
                for el in range(len(other.list[i])):
                    self.list[i][el] = self.list[i][el] + other.list[i][el]
            return matr1.__str__()
        else:
            print ("Невозможно сложить матрицы. Они имеют разный размер.")

matr1 = Martix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr1.__str__()

matr2 = Martix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
matr2.__str__()

matr1.__add__(matr2)