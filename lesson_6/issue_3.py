class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])

position = Position('John', 'Wick', 'Killer', {"wage": 10000, "bonus": 100000000})
position.get_full_name()
position.get_total_income()
