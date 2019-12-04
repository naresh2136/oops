Method Overriding in Python
Method overriding is a concept of object oriented programming that allows us to change the implementation of
a function in the child class that is defined in the parent class. It is the ability of a child class to change
the implementation of any method which is already provided by one of its parent class(ancestors).

Following conditions must be met for overriding a function:

Inheritance should be there. Function overriding cannot be done within a class. We need to derive a child class from a parent class.
The function that is redefined in the child class should have the same signature as in the parent class i.e. same number of parameters.
As we have already learned about the concept of Inheritance, we know that when a child class inherits a parent class it also get access
to it public and protected(access modifiers in python) variables and methods, for example,




    parent


    class
        class Animal:
            # properties
            multicellular = True
            # Eukaryotic means Cells with Nucleus
            eukaryotic = True

            # function breath
            def breathe(self):
                print("I breathe oxygen.")

            # function feed
            def feed(self):
                print("I eat food.")


    # child class
    class Herbivorous(Animal):

        # function feed
        def feed(self):
            print("I eat only plants. I am vegetarian.")


    herbi = Herbivorous()
    herbi.feed()
    # calling some other function
    herbi.breathe()