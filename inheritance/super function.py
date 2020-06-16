class Parent:
    def __init__(self, name):
        print("Parent __init__", name)


class Parent2:
    def __init__(self, name):
        print("Parent2 __init__", name)


class Child(Parent2, Parent):   # super class is that class which inherit first (1, 2)
    def __init__(self):
        print("Child __init__")
        super().__init__("Anindo")      # super class
        Parent.__init__(self, "Turjo")  # second parent class


child_obj = Child()
print(Child.__mro__)            # memory resolution order
