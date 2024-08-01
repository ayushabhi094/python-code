# __str__ method in Python represents the class objects as a string
from typing import Any


class Employee:
    def __init__(self,name , book_name, age):
        self.name = name
        self.book_name = book_name
        self.age =  age

    def __len__(self):
        return self.age

    def __str__(self):
         return f"my name is {self.name} and my book name is {self.book_name} and my age is {self.age}"
     
    def __repr__(self):
         return f"my name is {self.name} and my book name is {self.book_name} and my age is {self.age}" 

    def __call__(self):
        print("call method is called")

obj = Employee("Ayush", "harry Potter", 23)
# print(obj)
# print(len(obj))
print(obj.__str__())
print(obj.__repr__())
obj()
# list1 = [1,2,23,4,5,5,566,6]
# print(len(list1))