# def cube(n):
#     return n*n*n

# list = [1,2,3,45,5,66,7]
# newL = []
# for i in list:
#     newL.append(cube(i))

# print(newL)


# map function applies a function  to each element of iterator and return a new sequence containing the transformed element

# map function return object we have to change it to desired type

# map(function, iterable)

# def cube(l1):
#     return l1*l1*l1

# l1 = [1,2,3,4,5,6,7,8]
# map_list = map(cube, l1)
# print(list(map_list))



# L2 = [1,2,3,45,6]
# map_list2 = map(lambda x: x*x*x, L2)
# print(list(map_list2))

# filter(function, iterable)
# filter function filters a sequence of elements based on the given predicate(a function that returns a boolean value) and returns a new sequence that containing only the element that meet the predicate


# def function(a):
#     return a>4

# l3 = [1,2,3,4,5,6,7,8,9]
# new_list_filter = filter(function, l3)
# print(list(new_list_filter))



# reduce function :- we have to import reduce and it reduce to a single value and provide me a final result
# reduce(function , iterable)

import functools

reduce_list = [1,2,3,4,5]

# new_reduce = functools.reduce(lambda x,y: x+y, reduce_list)
# print(new_reduce)
def sum_list(x,y):
    return x+y

reduce_new = functools.reduce(sum_list , reduce_list)
print(reduce_new)