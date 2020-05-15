class Employee:
    salary = 25000
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def printdata(self):
        return f"Your name is {self.name} \n and your age is {self.age}  and your city is  {self.city}"

    @classmethod #classmethod doesn't require self
    def ChangeSalary(cls,NewSalary):
        cls.salary = NewSalary





light = Employee("Yeshu" , 19, "Pune")
print(light.printdata())
print(light.salary)
Employee.salary = 27000
light.ChangeSalary(30000)
print(light.salary)