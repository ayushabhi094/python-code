
# this will give integer type if we declare this single element in tuple
# tup = (1)
# print(type(tup))
# print(tup)


# so we have to give one element like this
# tup = (1,)
# tup[0] = 99   tuple are unchangable
# print(type(tup))
# print(tup)

t = (1,2,3,4,5,6,7,8,9)
if 10 in t:
    print("yes")
else:
    print("no")

print(t[2:4])