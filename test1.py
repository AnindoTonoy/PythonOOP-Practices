class Student():
    def __init__(self):
        self.name = 'Anindo'
        self.age = 24
        self.marks =95

    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)

s1 = Student()
s1.name = "Turjo"
print(s1.name + "\n")
print('ID of S1 - ', id(s1))

s2 = Student()
print(s2.talk())
print('ID of S2 - ',  id(s2))