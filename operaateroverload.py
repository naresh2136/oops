
Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator +
is used to add two integers as well as join two strings and merge two lists.
It is achievable because ‘+’ operator is overloaded by int class and str class.
You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this
is called Operator Overloading.


class A:
    def __init__(self, a):
        self.a = a

        # adding two objects

    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)


Output:

3
GeeksFor


----------------------------------------------------------------


class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)
Output:

ob1 is lessthan
ob2
Not
equal

---------------------------------------
__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
