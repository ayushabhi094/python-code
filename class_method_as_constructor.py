# class method used as a alternative constructor
# class Employee:
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromString(cls,string):
#         return cls(string.split("-")[0], int(string.split("-")[1]) )

# string1 = "Ayush-22"
# obj = Employee.fromString(string1)
# print(obj.name)
# print(obj.age)



class Professor:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no =roll_no
        self.age = age

    @classmethod
    def from_string_details(cls,string):
        return cls(string.split(",")[0], int(string.split(",")[1]), int(string.split(",")[2]) )
    

obj = Professor.from_string_details("Jack Robins,2233394,45")
print(obj.name)
print(obj.roll_no)
print(obj.age)
