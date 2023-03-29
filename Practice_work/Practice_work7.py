from math import floor, ceil


class Snow:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        self.count += other
        print('The number of snowflakes has been increased!')

    def __sub__(self, other):
        self.count -= other
        print('The number of snowflakes has been reduced!')

    def __mul__(self, other):
        self.count *= other
        print('The number of snowflakes has been increased!')

    def __truediv__(self, other):
        self.count = floor(self.count/other)

    def MakeSnow(self, k):
        num = self.count
        for i in range(ceil(self.count/k)):
            if num >= k:
                print('*'*k)
                num -= k
            else:
                print('*'*num)

    def __call__(self, n):
        self.count = n
        print('The number of snowflakes is overwritten')