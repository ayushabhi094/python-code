# private access modifier
class Employee:
    def __init__(self,n,age):
        self.__name  = n   #private variable
        self.__age = age  # private variable

e = Employee("private", 222)
print(e._Employee__name)  # to access private variable outside the class we can use _classname__variable_name it is called name mangling
print(e._Employee__age)