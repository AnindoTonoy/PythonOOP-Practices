# Defining a Class
class Student:

    # defining a constructor
    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m

    # action method
    def display(self):
        print("Hi", self.name)
        print("Your age is", self.age)
        print("Your marks:", self.marks)


# creating a instance of Student class
s1 = Student("Anindo", 24, English=95, Maths=97, Science=98)
# calling display() method to print name, age and marks
s1.display()

# print("- - - -")
#
# s2 = Student("Turjo", 18, 95)
# s2.display()
