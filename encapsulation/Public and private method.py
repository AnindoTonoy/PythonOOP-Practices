class Example:

    def __init__(self):
        self.x = 5
        self._y = 10
        self.__Z = 15

    # defining a public method
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__Z)
        self.__private_method()

    # defining a private method
    def __private_method(self):
        print("This is a Private method")


s = Example()
print(s.public_method())
