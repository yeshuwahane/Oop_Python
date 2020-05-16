# without using super
class Employee:
    salary = 25000

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def PrintData(self):
        return f"your name is {self.name} \n your age is {self.age} \n your city is {self.city}"

    @classmethod
    def ChangeSalary(cls, NewSalary):
        cls.salary = NewSalary

    # @classmethod
    # def from_str(cls, string):
    #     var = string.split("-")
    #     return cls(var[0], var[1], var[2])

class programmer(Employee):
    bonus = 43
    def __init__(self,name,age, city,list):
        self.name = name
        self.age = age
        self.list = list
        self.city = city

    def printprog(self):
        return f"The citizen of kothrud is {self.name} \n age is {self.age} \n  and language is {self.list}  "


light = Employee("Yeshu Wahane", 19, "Pune")
ashu = Employee("ashutosh ",21,"Pune")
darkclay = programmer("vaibhav ", 21, "Kothrud","python")
eliot = programmer("harsh", 20, "Kothrud", "python")

# print(darkclay.printprog())
# print(eliot.printprog())

# print(ashu.age)
# print(light.PrintData())
# print(Employee.salary)
# print(light.salary)
# light.ChangeSalary(30000)
# print(Employee.salary)
print(eliot.printprog())
print(darkclay.bonus)