# lambda function is an anonymous function without any name
# why we need lambda function we can pass lambda function as a argument also in another function

# lambda argument: expression

# def double(x):
#     return x*2

# double = lambda x: x*2
# cube = lambda x: x*x*x
# avg = lambda x,y: (x+y)/2

# print(double(5))
# print(cube(5))
# print(avg(2,4))





def appl(fx, value):
    return 2 + fx(value)
    
c  = appl(lambda x: x*x*x, 3)
print(c)
