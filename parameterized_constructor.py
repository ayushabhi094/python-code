# class Student:
#     def __init__(self, name , age, email):
#         self.name  = name
#         self.age  = age
#         self.email = email

# obj = Student("Ayush",22, "ayushabhi09@gmail.com")
# print(obj.name)

        

# list = [1,2,3,3,4,4,5,5,5,6,7,8]
# list = dict(fromkeys(list)) 

thisdic = {
    "name": "Ayush Jain",
    "email": "ayushabhi094@gmail.com",
    "age": 21
}


# for i in thisdic.keys():
#     print(i)


# for i in thisdic.values():
#     print(i)


# for x,y in thisdic.items():
#     print(x,y)


# x = ('key1', 'key2', 'key3')
# y = 0
# thisdic = dict.fromkeys(x,y)
# print(thisdic)



list1  = [1,2,23,4,4,5,5]
dic = list(dict.fromkeys(list1))
print(dic)