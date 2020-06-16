#Taking inputs from user
n = input("Your Name: ")
a = int(input("Your Age: "))
m = int(input("Your Marks: "))

#Defining a Class
class Student:

    # defining a constructor
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.marks = m

    # action method
    def display(self):
        print("Hi", self.name)
        print("Your age is", self.age)
        print("Your marks:", self.marks)


#creating a s1 instance of Student class
s1 = Student(n, a, m)
#calling display() method to print name, age and marks
s1.display()

print("- - - -")

#creating another s2 instance of Student class
s2 = Student("Turjo", 18, 95)
s2.display()
