import threading
import time


def test1(x, y):
    for i in range(x, y):
        print(threading.currentThread().getName(), i)
        time.sleep(1)


def test2(a, b):
    for j in range(a, b):
        print(threading.currentThread().getName(), j)
        time.sleep(1)


t1 = threading.Thread(target=test1, args=(2, 6))
t2 = threading.Thread(target=test2, args=(7, 11))

#t1.setName("tx1")
#t2.setName("tx2")

t1.start()
time.sleep(0.2)
t2.start()

t1.join()
t2.join()

print("This is main program..")



=============================================

from threading import *
from time import *


class Student():
    def show(self):
        for i in range(5):
            print('this is parent class')
            sleep(0.2)

    def show2(self):
        for i in range(5):
            print('this is child class')
            sleep(0.2)


s = Student()
t = Thread(target=s.show)
t1 = Thread(target=Student().show2)
t.start()
sleep(0.2)
t1.start()
t.join()
t.join()
print('this is main thread')


==============================================

from threading import *
from time import *


class Hello(Thread):
    def show(self):
        for i in range(5):
            print('hi this is prent')
            sleep(0.2)


class Hi(Thread):
    def saw(self):
        for i in range(5):
            print('hi this is child')
            sleep(0.2)


t1 = Hello()
t2 = Hi()

x = Thread(target=t1.show)
y = Thread(target=t2.saw)

x.start()
sleep(0.2)
y.start()
x.join()
y.join()
print('this is final')


=================================================

from threading import *
from time import *


class Demo():
    def num(self):
        for i in range(5):
            print('this is num', i)
            print(current_thread().getName())
            sleep(1)

    def duble(self):
        for i in range(5):
            print('this is dublenum', 2 * i)
            print(current_thread().getName())
            sleep(1)

    def square(self):
        for i in range(5):
            print('this is square', i * i)
            print(current_thread().getName())
            sleep(1)


obj = Demo()
t1 = Thread(target=obj.num)
t2 = Thread(target=obj.duble)
t3 = Thread(target=obj.square)

t1.start()
sleep(0.2)
t2.start()
sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print('this is main thread')






















