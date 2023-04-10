from random import randrange


class Data:
    def __init__(self, *items):
        self.item = tuple(items)

    def __getitem__(self, i):
        return self.item[i]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forget(self):
        i = randrange(len(self.knowledge))
        print(f'{self.knowledge[i]} wad beaten')
        del self.knowledge[i]

    def explore(self, *items):
        for i in items:
            if i not in self.knowledge:
                self.knowledge.append(i)


lessons = Data('history', 'geography', 'class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
t1 = Teacher()
s1 = Pupil()
s2 = Pupil()
t1.teach(lessons[2], s1, s2)
t1.teach((lessons[1]), s1)
s2.explore(lessons[3])
print(s1.knowledge)
print(s2.knowledge)
s1.forget()
s2.forget()
print(s1.knowledge)
print(s2.knowledge)