class People:
    people = dict()

    def __init__(self, age, orientation, profession):
        self.__age = age
        self.__orientation = orientation
        self.__profession = profession

    def __setattr__(self, key, value):  # Function for checking the attributes being created.
        if key == f'_{self.__class__.__name__}__age':
            self.__dict__[key] = value
        elif key == f'_{self.__class__.__name__}__orientation' and value.lower() in ('men', 'women'):
            self.__dict__[key] = value.title()
        elif key == f'_{self.__class__.__name__}__profession':
            self.__dict__[key] = value.title()
        else:
            raise NameError('You cannot create new attributes')

    def get(self, atr):  # Function to output the selected attribute
        return getattr(self, f'_{self.__class__.__name__}__{atr}', 'There is not such attribute')

    def set(self, atr, value):  # Function for changing selected attribute
        return setattr(self, f'_{self.__class__.__name__}__{atr}', value)


def create_user():  # Function for created person
    name = input('Enter the name: ').title()
    if name not in People.people:  # Checking the name in the list
        age = input('Enter the age: ')
        orientation = input('Enter the orientation: ')
        professional = input('Enter the profession: ')
        People.people[name] = People(age, orientation, professional)
    else:
        raise NameError('Such a name is in the list')


def delete_user():  # Function for delete person
    name = input('Enter the name: ').title()
    if name in People.people:
        del People.people[name]
        print(f'The {name} was deleted')
    else:
        raise NameError("Such name not in list")


def get_user():  # Function for output attribute.
    name = input('Enter the name: ').title()
    attr = dict([(1, 'age'), (2, 'orientation'), (3, 'profession')])
    if name in People.people:
            atr = int(input('1 - age\n2 - orientation\n3 - profession\nAnswer: '))
            print(People.people[name].get(attr[atr]))
            user = int(input('Continue: 1 - Yes\n2 - No\nAnswer: '))
            if user == 1:
                get_user()
    else:
        raise NameError


def set_user():
    name = input('Enter the name: ').title()
    attr = dict([(1, 'age'), (2, 'orientation'), (3, 'profession')])
    if name in People.people:
        atr = int(input('1 - age\n2 - orientation\n3 - profession\nAnswer: '))
        if atr == 1:
            value = int(input('Enter the value: '))
        else:
            value = input('Enter the value: ')
        People.people[name].set(attr[atr], value)
        user = int(input('Continue: 1 - Yes\n2 - No\nAnswer: '))
        if user == 1:
            set_user()
    else:
        raise NameError


def menu():
    print(f'0 - Show peoples\n1 - Create a person\n2 - Delete a person\n3 - Get a person\n4 - Set a person\n5 - Close')


def show_list():
    print(f'Users:', end=' ')
    print(*People.people.keys(), sep=', ')


print("Hello")
menu()
user = int(input('Answer: '))
while user in (0, 1, 2, 3, 4, 5):
    if user == 0:
        show_list()
        input()
        menu()
        user = int(input('Answer: '))
    elif user == 1:
        create_user()
        input()
        menu()
        user = int(input('Answer: '))
    elif user == 2:
        delete_user()
        input()
        menu()
        user = int(input('Answer: '))
    elif user == 3:
        get_user()
        input()
        menu()
        user = int(input('Answer: '))
    elif user == 4:
        set_user()
        input()
        menu()
        user = int(input('Answer: '))
    elif user == 5:
        break
    else:
        raise ValueError('Invalid value')
print('Goodbye!!!')
