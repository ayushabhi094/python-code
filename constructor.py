class Person:
    def __init__(self, n ,o):
        self.name = n
        self.occupation = o
    
    def info(self):
        print(f"my name is {self.name} and my occupation is {self.occupation}")

obj = Person("Ayush", "Python developer")
obj.info()  
obj1 = Person("Divya", "HR")
obj1.info() 