# dir(), help() method in python

#  __dict__ keyword

# dir() method return the list of all the attributes and methods(including dunder method) available for object

# x = [1,2,3,45,5,6,7]
# y = [8,9]
# print(dir(x))
# print(x.__add__(y))



# __dict__ keyword in python: returns a dictionary represention of and 

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.version = 1

# p = Person("ayush", 20)
# print(p.__dict__)


# print(help(Person))



y = (1,2,3,4,5,6,6)
print(dir(y))
