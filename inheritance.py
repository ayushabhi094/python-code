# time_list = [12, 2, 32, 19, 57, 22, 14]
# print(min(time_list))
# print(max(time_list))



# time_list = [12, 2, 32, 19, 57, 22, 14]
# print(sorted(time_list))

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the details of employee name is {self.name} and id is {self.id}")

class Programmer(Employee):
    def showDetailsProgrammer(self):
        print(f"this is child definition")


emp = Employee("Ayush", 100)
emp.showDetails()

p = Programmer("Ram", 20)
p.showDetails()
p.showDetailsProgrammer()

