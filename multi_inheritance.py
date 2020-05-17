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

class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printDetail(self):
        return f"Name is {self.name} \n Game is {self.game}"

class CoolEmploy(Employee,Player):
    lang = "python"
    def printlan(self):
        print(self.lang)





light = Employee("Yeshu Wahane", 19, "Pune")
ashu = Employee.from_str("ashutosh - 21 - Pune")
# print(ashu.age)
# print(light.PrintData())
# print(Employee.salary)
# print(light.salary)
# light.ChangeSalary(30000)
# print(Employee.salary)

harsh = Player("harsh","Cricket")
vaibhav = CoolEmploy("Vaibhav",4500,"Cool programmer")
# vaibhav.PrintData()
# print(vaibhav.PrintData())
# vaibhav.printlan()
print(vaibhav.salary)