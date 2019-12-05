

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables
and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be
changed by an object’s method. Those type of variables are known as private varibale.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.


private
methods:


class car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print('driwing')

    def __updatesoftware(self):
        print('updating software')


blackcar = car()
blackcar.drive()

output:
updating software
driwing
==================================================

class car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print('driwing')

    def __updatesoftware(self):
        print('updating software')

blackcar=car()
blackcar.drive()
blackcar.__updatesoftware()

output:
shows error because of __ update is a private method we cont accet outside the classmethod
but we can call with in the class as like the above programm