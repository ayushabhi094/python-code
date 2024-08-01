class Employee:
    companyName = "Apple"   #class variable can we used in any method in class
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name      #instance variable with self
        self.raise_amount = 100 #instance variable with self 
        Employee.noOfEmployee +=1

    def showDetails(self):
        print(f"print the name of the employee {self.name} and raise amount is {self.raise_amount} and company name is {self.companyName} and company size is {self.noOfEmployee}")

emp = Employee("Ayush")
Employee.companyName = "Google"
# print(Employee.companyName)
emp.raise_amount = 99.00
emp.companyName = "samsung"  # in this instance variable will be overwrite with class variable
emp.showDetails()


emp1 = Employee("Harry")
emp1.showDetails()
