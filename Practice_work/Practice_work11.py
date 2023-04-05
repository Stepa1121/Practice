from random import uniform


def generator(quantity, *band):
    for _ in range(quantity):
        yield uniform(band[0], band[1])


a = generator(4, 1, 5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


