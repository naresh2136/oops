

'''for call a particular method in super class'''

class A:
    def m1(self):
        print('A class method')


class B(A):
    def m1(self):
        print('B class method')


class C(B):
    def m1(self):
        print('C class method')


class D(C):
    def m1(self):
        print('D class method')


class E(D):
    def m1(self):
        print(' E class method')
        A.m1(self)
        B.m1(self)


e = E()
e.m1()
print(D.mro())
c = C()
c.m1()