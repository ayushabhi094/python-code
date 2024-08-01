class Employee:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return  Employee(self.val + other.val)

    def print_details(self):
        print(f"the total value is {self.val}")

obj1 = Employee("Geeks")
obj2 = Employee("ForGeeks")
obj3 = obj1+ obj2
obj3.print_details()

