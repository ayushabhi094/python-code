# protected access modifier is used to describe (attributes or method) that is accessed by class itself or sub class 
class Employee:
    def __init__(self,n,age):
        self._name  = n   #protected variable
        self._age = age  # protected variable

    def showDetails(self):
        return "hi this is  protected method"

class Programmer(Employee):
    pass

# e = Employee("protected", 10121)
# print(e._name)
# print(e._age)

# called by object of Programmer class
pro = Programmer("protected", 10121)
print(pro._name)
print(pro._age)
print(pro.showDetails())