class Polygon:
    __height = None
    __width = None

    def set_value(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width


# inherited from Polygon class
class Square(Polygon):
    def area(self):
        return self.get_height() * self.get_width()


# inherited from Polygon class
class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() * 1/2


s1 = Square()
h = int(input("enter the height:"))
w = int(input("enter the width:"))
s1.set_value(h, w)
print("Area of Square =", s1.area())

print("----")

t1 = Triangle()
t1.set_value(7, 8)
print("Area of Triangle =", t1.area())