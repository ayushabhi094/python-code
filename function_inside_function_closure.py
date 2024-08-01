# closure in function +python
# In Python, inner functions can access variables defined in the outer function's scope through a concept known as closures. This means that variables defined in the outer function are accessible within the inner function even after the outer function has finished executing.
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()


# Even though x is not directly defined inside myinnerfunc(), Python looks for x first in the local scope of myinnerfunc(). Since x is not found there, Python then looks in the enclosing scopes (in this case, the scope of myfunc() where x is defined). This ability to access variables from enclosing scopes is what allows myinnerfunc() to access and print the value of x.