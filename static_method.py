# static method are method that can be called from class itself only and we generally use @staticmethod decorator for this

class Employee:
    @staticmethod
    def add(x,y):
        return x+y

print(Employee.add(2,4))