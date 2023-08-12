class ParentClass:
    def __init__(self) -> None:
        print("This is The Parent Class")


class ChildClass(ParentClass):
    pass


childObject = ChildClass()
# class FirstClass:
#     thenumberofInsatanse = 0

#     def __init__(self, firstname, lastname, phonenumber) -> None:
#         self.firstname = firstname
#         self.lastname = lastname
#         self.phonenumber = phonenumber
#         FirstClass.thenumberofInsatanse += 1

#     def __str__(self) -> str:
#         return f"Myname is {self.firstname+self.lastname} \nMyPhonenumber is {self.phonenumber}"

#     def printMyInstanteData(self):
#         pj = self.phonenumber
#         return f"Myname is {self.firstname+self.lastname} \nMyPhonenumber is adkuyilusdt;iu {pj}"

#     @classmethod
#     def printThe_number(cls):
#         return f"The number of objects {cls.thenumberofInsatanse}"

#     @staticmethod
#     def first_static_method():
#         return f"this is the First Static Method in python"


# print(FirstClass.thenumberofInsatanse)
# firstObject = FirstClass("Abdelrahman", "Shoaib", ("01063103655"))
# firstObject1 = FirstClass("Abdelrahman", "Shoaib", ("01063103655"))
# firstObject2 = FirstClass("Abdelrahman", "Shoaib", ("01063103655"))
# firstObject3 = FirstClass("Abdelrahman", "Shoaib", ("01063103655"))
# print(FirstClass.thenumberofInsatanse)

# print("#" * 100)
# print(FirstClass.first_static_method())
# print("#" * 100)
# print(firstObject.printMyInstanteData())
# print("#" * 100)
# print(FirstClass.printMyInstanteData(firstObject))
# print("#" * 100)
# print(FirstClass.printThe_number())
# print("#" * 100)
# print("fff", str(firstObject))
