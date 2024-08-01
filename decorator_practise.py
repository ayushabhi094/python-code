def greet(func):
    def inner(*args):
        print("hello good morning")
        func(*args)
        print("hello good afternoon")
    return inner

# @greet
# def hello():
#     print("hello everyone")

# hello()
@greet
def add(a,b):
    print(a+b)

add(2,4)