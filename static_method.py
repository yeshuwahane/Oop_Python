class Employee:
    salary = 25000
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def printdata(self):
        return f"Your name is {self.name} \n Your age is {self.age} \n Your cityt is {self.city} "

    @classmethod
    def ChangeSalary(cls,Newsalary):
        cls.salary = Newsalary

    @staticmethod
    def printq():
        print("Static method is working")



light = Employee("Yeshu Wahane" ,19 , "Pune")
print(light.printdata())
light.ChangeSalary(45000)
# light.ChangeSalary()
# print(light.salary)
# print(light.salary)
# print(Employee.salary)
# light.printq()
light.printq()
