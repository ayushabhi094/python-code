class Employee:
    company = "TATA"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"my name is {self.name} and my company is {self.company}")

    @staticmethod
    def static_method(age):
        if age > 20:
            print("you are above 20")
        else:
            print("you are below 20")   
        
    @classmethod
    def class_method_name(cls, my_company):
        cls.company = my_company

a = Employee("Ayush", 22)
b = Employee("Rahul", 25)
Employee.class_method_name("Hero")
Employee.static_method(24)
a.show()
b.show()
