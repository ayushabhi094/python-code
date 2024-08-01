# method overrriding is a same method name in derived class as in base class with same parameter and by calling that metthod through derived class instance it will call derived class method , so to access base class method we can use super function to access base class method through derived class instance

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
       return self.x*self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        print("calculating area of circle")
        return 3.14*super().area()
    
obj = Circle(5)
c = obj.area()
print(c)