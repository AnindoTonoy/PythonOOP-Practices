class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay * 12) + self.reward


class Employee:
    def __init__(self, name, position, sal):
        self.name = name
        self.position = position
        self.final_salary = sal   # aggregation of Salary class

    def final_salary_m(self):
        return self.final_salary.annual_salary()


sal = Salary(100000, 15000)
emp = Employee("Anindo", "Py dev", sal)
print("Employee Name:", emp.name + "\n" + "Position:", emp.position)
print("Annual Salary:", emp.final_salary_m())
