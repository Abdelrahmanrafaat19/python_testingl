class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.name = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    def display(self):
        print(f"value: {self.name}, class_variable: {self.class_variable}")


# Creating instances of the class
obj1 = MyClass(10)
obj2 = MyClass(20)
obj1._MyClass__name = 20
# Accessing and invoking the class method
obj1.increment_class_variable()
obj1.class_variable

# Displaying the class variable for both instances
obj1.display()
obj2.display()
print(dir(obj1))
