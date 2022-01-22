class Road:

    weight_1sm = 25
    sm = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):

        return self._length * self._width * self.weight_1sm * self.sm

    
asd = Road(5, 2)
print(asd.calculation())
