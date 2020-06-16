from abc import ABC, abstractmethod


# abstract Shape class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


square_obj = Square(5)
print(square_obj.area())
print(square_obj.perimeter())