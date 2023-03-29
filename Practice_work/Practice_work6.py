class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.wd = []

    def add_wd(self):  # Function for add a class "WinDoor"
        user = int(input('Enter how many windows and doors: '))
        for i in range(1, user + 1):
            print(f'{i} objects')
            user_width = int(input('Enter the width: '))
            user_length = int(input('Enter the length: '))
            self.wd.append(WinDoor(user_length, user_width))

    @staticmethod
    def rolls():
        roll_width = int(input('Enter the width for roll: '))
        roll_length = int(input('Enter the length for roll: '))
        return roll_length * roll_width

    def full_square(self):
        return 2 * self.height * (self.length * self.length)

    def pasted_square(self):
        new_square = self.full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square, new_square/self.rolls()

    def change_size(self):
        print('1 - width\n2 - length\n3 - height')
        user = int(input('Enter the parameter: '))
        if user in (1, 2, 3):
            if user == 1:
                self.width = int(input())
            elif user == 2:
                self.length = int(input())
            else:
                self.height = int(input())
        else:
            raise ValueError


def create_room():
    l = int(input('Enter the length: '))
    w = int(input('Enter the width: '))
    h = int(input('Enter the height: '))
    i = Room(w, l, h)
    i.add_wd()
    f = i.full_square()
    p = i.pasted_square()
    print(f'Full square: {f}')
    print(f'Pasted square: {p[0]} and need {p[1]} rolls')
    user = int(input('Continue?\n1 - Yes\n2 - No\nAnswer: '))
    if user == 1:
        create_room()


create_room()