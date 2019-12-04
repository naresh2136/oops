class DUCK:
    def talk(self):
        print('quck..quck')


class HUMAN:
    def talk(self):
        print('hello.hi')

class DOG:
    def bark(self):
        print('BOW>>BOW')


def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
         obj.brak()

d=DUCK()
f1(d)

d=DOG()
f1(d)

h=HUMAN()
f1(h)




