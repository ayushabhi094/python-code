# enumerate function is a build in function in python that allows you to loop over a sequences 
# (list, tuple , dictionaries) and get index and values of each element in the sequence at the same time

list = [1,2,3,4,5,6,7,8,9]
for index, value in enumerate(list):
    # print(index,value)
    print(index, value)
    if (index == 3):
        print("hi awesome we found index 3")