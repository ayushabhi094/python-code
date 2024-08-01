class Person:
    name = "Harry"
    occupation = "software developer"

    def info(self):
        print(f"my name is {self.name} and my accupation is {self.occupation}")

obj1 = Person()
obj2 = Person()
obj3 = Person()
obj1.name = "Ram"
obj1.occupation = "HR"

obj2.name = "shyam"
obj2.occupation = "IT"

obj1.info()
obj2.info()
obj3.info()