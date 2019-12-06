class car:
    __maxspeed=0
    __name=''

    def __init__(self):
        self.__maxspeed=200
        self.__name='supercar'

    def drive(self):
        print('driving')
        print(self.__maxspeed)

    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)

redcar=car()
redcar.drive()
redcar.setspeed(100)

output:
driving
200
100

=======================================

class car:
    __maxspeed=0
    __name=''

    def __init__(self):
        self.__maxspeed=200
        self.__name='supercar'

    def drive(self):
        print('driving')
        print(self.__maxspeed)


redcar=car()
redcar.drive()
redcar.__maxspeed=100
redcar.drive()

output:
drive
200
drive
200

'here the value of the __maxspeed is not changed to 100 because of that is private variable'
'so private variaables are cont change out side of the calss'