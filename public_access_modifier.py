# public access modifier
class Employee:
    def __init__(self,n,age):
        self.name  = n   #public variable
        self.age = age  # public variable

e = Employee("Assss", 1000)
print(e.name)
print(e.age)



