
class Cell:
    def __init__(self, number):
        self.number = number

    def ___add__(self):
        cell = cell_1.number + cell_2.number
        return print("Результат сложения:", cell)

    def __sub__(self):
        if cell_1.number > cell_2.number:
            dif = cell_1.number - cell_2.number
            return print("Результат вычитания:",dif)
        else:
            return print("Вычитание невозможно!")

    def __mul__(self):
        cell = cell_1.number * cell_2.number
        return print("Результат умножения:",cell)

    def ___truediv__(self):
        cell = cell_1.number // cell_2.number
        return print("Результат деления:",cell)

    def make_order(self, range_number):
        for i in range(self.number // range_number):
            print("*" * range_number)
        print('*' * (self.number % range_number))

cell_1 = Cell(12)
cell_2 = Cell(5)
cell_1.___add__()
cell_1.__sub__()
cell_1.__mul__()
cell_1.___truediv__()
cell_1.make_order(5)