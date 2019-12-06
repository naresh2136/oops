class Test:
    x = 10
    _y = 20
    __z = 30

    def m1(self, a, b):
        self._a = a
        self.__b = b
        print(self._a)
        print(Test.x)
        print(Test._y)
        print(Test.__z)


t = Test()
t.m1(40, 50)
print(t._a)
print(t._Test__b)
print(Test.x)
print(Test._y)
print(t._Test__z)

'in the above program we are created static,instance variables decleare the private attributes and call out side the class and we get the values also'

===================================================

class Test:
    x = 10
    _y = 20
    __z = 30

    def __init__(self, k, l, m):
        self._k = k
        self.__l = l
        self.__m = m
        print(Test._y)
        print(Test.__z)
        _Q = 100
        __R = 200
        print(_Q)
        print(__R)

    def m1(self, a, b):
        self._a = a
        self.__b = b
        print(self._a)
        print(Test.x)
        print(Test._y)
        print(Test.__z)
        print(self._k)
        print(self.__m)


t = Test(40, 50, 60)
t.m1(70, 80)
print(t._y)
print(t._Test__z)
print(t._k)
print(t._Test__l)
print(t._Test__m)
print(t._a)
print(t._Test__b)

'in the above programe we create static variables and instance variable'
'access those variables outside the class also'

#print(_Q)the are available only in side the specific function

oytput:
20
30
70
10
20
30
40
60
20
30
40
50
60
70
80




