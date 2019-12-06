class person:

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def display(self):
        print('name:', self._name)
        print('age:', self.__age)


class student(person):

    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    # print('name:',self._name)
    # print('age:',self.__age)

    def display(self):
        super().display()
        print('roll no:', self.roll)
        print('marks:', self.marks)


k = person('kiran', 35)
print('name:', k._name)
print('age:', k._person__age)
s1 = student('ajay', 22, 90, 100)
s1.display()


#in oops private variables are can access outside of the class
#but not access in side another class when use inheritence