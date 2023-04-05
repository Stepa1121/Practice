from random import uniform


class Num:
    def __init__(self, quantity, *band):
        self.q = quantity
        self.b = band

    def __iter__(self):
        return self

    def __next__(self):
        if self.q == 0:
            raise StopIteration
        self.q -= 1
        return uniform(self.b[0], self.b[1])


rand = Num(5, 0, 3)
for i in rand:
    print(round(i, 2))