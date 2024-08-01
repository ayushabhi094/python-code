# Generators are special type of function that allow yout to generate iterable sequence of value
# A generator function return a generator object,which can be used to generate a value one by one as you iterate over it



# def generatorfunction():
#     for i in range(5):
#         yield i

# # result = generatorfunction()
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))

# for value in generatorfunction():
#     print(value)


def generator_function():
    n = 1
    while n < 10:
        sq = n*n
        yield sq
        n += 1 

for value in generator_function():
    print(value)

