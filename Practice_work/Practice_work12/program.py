from Windoor import *


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