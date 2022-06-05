class Cell:

    def __init__(self, size) -> None:
        self.size = size


    def __add__(self, other):

        return self.size + other.size

    def __sub__(self, other):

        res = self.size - other.size

        if(res > 0):
            
            return res
        else:
            print("Разница меньше 0")


    def __mul__(self, other):

        res = self.size * other.size

        return res

    def __truediv__(self, other):

        return round(self.size / other.size)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.size // rows)]) + '\n' + '*' * (self.size % rows)


c1 = Cell(5)
c2 = Cell(2)
print(c1 + c2)
print(c1 * c2)
print(c1.make_order(2))