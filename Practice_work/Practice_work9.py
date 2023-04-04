from math import pi


class CyLinder:
    @staticmethod
    def Make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2+side, 2)

    def __init__(self, diameter, high):
        self.__dict__['dia'] = diameter
        self.__dict__['h'] = high
        self.__dict__['area'] = self.Make_area(diameter, high)

    def __setattr__(self, key, value):
        if key == 'dia':
            self.__dict__['dia'] = value
            self.__dict__['area'] = self.Make_area(self.__dict__['dia'], self.__dict__['h'])
        elif key == 'h':
            self.__dict__['h'] = value
            self.__dict__['area'] = self.Make_area(self.__dict__['dia'], self.__dict__['h'])
        elif key == 'area':
            print("You can't change area directly")
        else:
            print("Can't create new attributes")

    def show_area(self):
        print(self.__dict__['area'])


s = CyLinder(10, 10)
s1 = CyLinder(20, 20)
s1.show_area()
s1.dia = 10
s1.show_area()




