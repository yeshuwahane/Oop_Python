class Employee:
    paise = 14
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role


    def printDetail(self):
        return f"Name is {self.name} \n Salary is {self.salary} \n Role is {self.role} "



light = Employee("Yeshu", 15000,"developer")
#light.name = "yeshu"
#light.salary = 15000
#light.role = "developer"
print(light.printDetail())