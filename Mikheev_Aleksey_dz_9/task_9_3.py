class Worker:

    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']