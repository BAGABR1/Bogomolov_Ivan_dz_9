class Worker:
    position = 'program'

    def __init__(self, name, surname, position, w, b):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": w, "bonus": b}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Полный доход сотрудника: {self._income['wage'] + self._income['bonus']}")


example = Position('Mike', 'Vasovski', 'Assistant', 32000, 18500)
print(example.name)
print(example.surname)
print(example.position)
print(example._income)
example.get_full_name()
example.get_total_income()
