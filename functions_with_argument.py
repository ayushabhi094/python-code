# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i 
#     return sum/len(numbers)

# c = average(5,6,7)
# print('Average is ', c)

# argument passed as a dictionary

# def DicName(**name):
#     print(name['fname'], name['middlename'], name['lname'])

# DicName(fname = "ayush", middlename = "kumar", lname = "jain")

def tupleData(*name):
    # print("Hello",name[0], name[1], name[2], name[3])
    for i in name:
        print(i)

tupleData("Red", "Yellow", "Blue", "Green")