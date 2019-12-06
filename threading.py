run() − The run() method is the entry point for a thread.

start() − The start() method starts a thread by calling the run method.

join([time]) − The join() waits for threads to terminate.

isAlive() − The isAlive() method checks whether a thread is still executing.

getName() − The getName() method returns the name of a thread.

setName() − The setName() method sets the name of a thread.

Creating Thread Using Threading Module

=============================================================

Without creating a class
Multithreading in Python can be accomplished without creating a class as well. Here is an example to demonstrate the same:

Example:
from threading import *
print(current_thread().getName())
def mt():
    print("Child Thread")
child=Thread(target=mt)
child.start()
print("Executing thread name :",current_thread().getName())
Output:

MainThread
Child Thread
Executing thread name : MainThread


==================================================

By extending the Thread class:
When a child class is created by extending the Thread class, the child class represents that a new thread is executing some task. When extending the Thread class, the child class can override only two methods i.e. the __init__() method and the run() method. No other method can be overridden other than these two methods.

Here is an example of how to extend the Thread class to create a thread:

Example:


import threading
import time
class mythread(threading.Thread):
    def run(self):
        for x in range(7):
        print("Hi from child")
a = mythread()
a.start()
a.join()
print("Bye from",current_thread().getName())
Output:
Hi from child
Hi from child
Hi from child
Hi from child
Hi from child
Hi from child
Hi from child
Bye from MainThread


====================================
Without Extending Thread class
To create a thread without extending the Thread class, you can do as follows:
Example:
from threading import *
class ex:
def myfunc(self): #self necessary as first parameter in a class func
    for x in range(7):
        print("Child")
myobj=ex()
thread1=Thread(target=myobj.myfunc)
thread1.start()
thread1.join()
print("done")
Output:

Child
Child
Child
Child
Child
Child
Child
done

The child thread executes myfunc after which the main thread executes the last print statement.