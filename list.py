# l = [91,2,3,4,"Ayush", True]
# print(type(l))
# print(l)
# print(l[1])
# print(l[0])

# if 92 in l:
#     print("yes")
# else:
#     print("no")

# colors  = ["Red", "Yellow", "Green", "Blue"]
# if "yellow" in colors:
#     print("Yellow is present")
# else:
#     print("Yellow is not present")


# same applies for string as well !
# if "Ry" in "Harry":
#     print("yes")
# else:
#     print("no")


# animals  = ["cat", "dog", "bat", "pig", "mouse"]
# print(animals[2:])
# print(animals[:4])
# print(animals[1:5:2])


# List comprehension
# animalsWith_0 = [item for item in animals if "a" in item]
# print(animalsWith_0)



# lst = [i*i for i in range(4) if i%2==0]
# print(lst)

# names =  ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if (len(item)>=5) ]
# print(namesWith_O)


# append method changes original list
# list = [1,2,3,4,5,6,7,8,8,8]
# list.append(9)
# list.sort()
# list.sort(reverse=True)
# list.reverse()
# print(list.index(3))
# print(list.count(8))
# print(list)

# l = [1,2,3,4,5,6,7,8,8,8]

# m = l.copy()
# m[0] = 0
# print(l.count(8))
# print(l)
# print(m)

l = [1,2,3,4,5,6,7,8,8,8]
# l.insert(1, 899)
# print(l)


m = [100,200,300,400,500]
k = l+m
# l.extend(m)
# print(l)

print(k)