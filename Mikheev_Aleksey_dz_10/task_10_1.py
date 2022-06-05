
class Matrix:

    def __init__(self, mt : list ):
        self.mt = mt


    def __str__(self) -> str:
        string = '';
        for row in self.mt:
            new_str = " ".join(map(str, row))
            string  = string + new_str + "\n"

        return string

    def test(self):
        print(len(self.mt)) 
        return 1
        for i, x in enumerate(self.mt):
            print(x, i)

            for b, y in enumerate(x):
                print(y, b)


    def __add__(self, other):

        if(len(self.mt) == len(other.mt) and len(self.mt[0]) == len(other.mt[0])):
            for i, x in enumerate(self.mt):
                for b, y in enumerate(x):
                    self.mt[i][b] = y + other.mt[i][b]


        else:
            print("Матрицы разного формата")

        return self

mt = Matrix([[1, 2, 3], [1, 2, 3], [3, 2, 1]])
mс = Matrix([[4, 3, 3], [1, 2, 3], [3, 2, 1]])
mt + mс

print(mt)