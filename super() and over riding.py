class A:
    classvar1 = "I am in class A"
    def __init__(self):
        self.var1 = "Class A constructor"
        self.classvar1 = "Hello world"
        self.special = "Special"

class B(A):
    classvar1 = "I am in Class B"

    def __init__(self):

        self.var1 = "Class B constructor"
        self.classvar1 = "Hello world  hii !"
        super().__init__()
        print(super().classvar1)

a = A()
b = B()

print(b.special,b.var1,b.classvar1)