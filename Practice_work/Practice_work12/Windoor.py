class WinDoor:
    def __init__(self, x, y):
        """Module for area window or door calculation"""
        self.square = x * y


class Room:
    def __init__(self, width, length, height):
        """Constructor accepts length, height, width and list of area windows and doors"""
        self.width = width
        self.length = length
        self.height = height
        self.wd = []

    def add_wd(self):  # Function for add a class "WinDoor"
        """Module for add areas of windows and doors"""
        user = int(input('Enter how many windows and doors: '))
        for i in range(1, user + 1):
            print(f'{i} objects')
            user_width = int(input('Enter the width: '))
            user_length = int(input('Enter the length: '))
            self.wd.append(WinDoor(user_length, user_width))

    @staticmethod
    def rolls():
        """Module for area roll calculation"""
        roll_width = int(input('Enter the width for roll: '))
        roll_length = int(input('Enter the length for roll: '))
        return roll_length * roll_width

    def full_square(self):
        """Module for full area calculation"""
        return 2 * self.height * (self.length * self.length)

    def pasted_square(self):
        """Module for pasted area calculation."""
        new_square = self.full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square, new_square/self.rolls()

    def change_size(self):
        """Module for change size length, width or height"""
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
