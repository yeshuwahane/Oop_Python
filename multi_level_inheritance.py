class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def Isdance(self):
        return f"Yes I  dance {self.dance}"


class Gson(Son):
    dance = 6

    def Isdance(self):
        return f"yeah! " \
               f"Yes i dance very good {self.dance} no. of forms"


Daddy = Dad()
light = Son()
harry = Gson()

print(harry.Isdance())

print(light.Isdance())
print(harry.basketball)