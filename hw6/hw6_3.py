
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print("Полное имя сотрудника: ", self.name, self.surname)

    def get_total_income(self):
        total_income = sum(self._income.values())
        print("Доход сотрудника с учетом премии: ", total_income)

worker1 = Position("Ivan", "Ivanov", "Teacher", 50, 10)
print(f"Имя: {worker1.name}; Фамилия: {worker1.surname}; Должность: {worker1.position}; Доход: {worker1._income}")
worker1.get_full_name()
worker1.get_total_income()