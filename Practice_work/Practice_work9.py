from math import pi


class CyLinder:
    @staticmethod
    def Make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2+side, 2)

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high
        self.__area = self.Make_area(diameter, high)

    def __setattr__(self, key, value):
        if key in (f'_{self.__class__.__name__}__area', 'dia', 'h'):
            self.__dict__[key] = value
            if hasattr(self, f'_{self.__class__.__name__}__area') and hasattr(self, 'dia') and hasattr(self, 'h'):
                self.__dict__[f'_{self.__class__.__name__}__area'] = self.Make_area(self.dia, self.h)

    def show_area(self):
        print(self.__area)


s = CyLinder(10, 10)
s1 = CyLinder(20, 20)
s1.show_area()
s1.dia = 10
s1.show_area()




