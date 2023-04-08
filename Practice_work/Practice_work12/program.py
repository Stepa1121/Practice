from Windoor import *
"""Function for working with user interface"""


def create_room():
    """Module for creating of room"""
    l = int(input('Enter the length: '))
    w = int(input('Enter the width: '))
    h = int(input('Enter the height: '))
    i = Room(w, l, h)  # Create a class "Room"
    i.add_wd()  # Addendum area of windows and doors.
    f = i.full_square()  # Full area calculation.
    p = i.pasted_square()  # Pasted area calculation.
    print(f'Full square: {f}')
    print(f'Pasted square: {p[0]} and need {p[1]} rolls')
    user = int(input('Continue?\n1 - Yes\n2 - No\nAnswer: '))
    if user == 1:
        create_room()


create_room()