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

    @classmethod
    def from_str(cls, string):
        var = string.split("-")
        return cls(var[0], var[1], var[2])


light = Employee("Yeshu Wahane", 19, "Pune")
ashu = Employee.from_str("ashutosh - 21 - Pune")
print(ashu.age)
# print(light.PrintData())
# print(Employee.salary)
# print(light.salary)
# light.ChangeSalary(30000)
# print(Employee.salary)
