# class Parent:
#     def isStudent1(self):
#         print("parent class called")

# class Child(Parent):
#      def isStudent2(self):
#         print("child class called")


# obj = Child()
# obj.isStudent1()
# obj.isStudent2()

class Animal:
    def __init__(self, name , color):
        self.name = name
        self.color = color

    def __str__(self):
      return  f"Animal name is {self.name} and animal color is {self.color}" 


class Cat(Animal):
    def __init__(self, name, color, bread):
        super().__init__(name, color)
        self.bread = bread


    def __str__(self):
        return f"cat name is : {self.name} and cat color is  {self.color} and cat bread is : {self.bread}"
    
obj = Cat("Billi", "Black", "cat")
print(obj)

ani = Animal("lion", "orange")
print(ani)