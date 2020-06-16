from square import Square as sq         # importing module from directory as 'sq'
from triangle import Triangle as tr     # importing module from directory as 'tr'


s1 = sq()
# getting inputs from user
h = int(input("enter the height: "))
w = int(input("enter the width: "))

s1.set_value(h, w)                     # setting the value h and w
s1.set_color("Blue")                   # setting the color for shape
print("Area of Square =", s1.area(), s1.get_color())

print("----")

t1 = tr()
t1.set_value(7, 8)
t1.set_color("Green")
print("Area of Triangle =", t1.area(), t1.get_color())