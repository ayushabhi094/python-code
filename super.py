# super() keyword is  useful for calling parent method from child method, we can also called parent constructor from child also

# class Parent:
#     def parent_class(self):
#         print("this is parent method")

# class Child(Parent):
#     def child_class(self):
#         print("this is child method")
#         super().parent_class()

# obj = Child()
# obj.child_class()
# obj.parent_class()


class computer():
    def __init__(self,ram , storage):
        self.ram = ram
        self.storage = storage
        print("parent constructor")

class mobile(computer):
    def __init__(self, ram , storage):
        super().__init__(ram , storage)
        self.model = "i phone"
        print("child constructor")    

obj = mobile("8gb",'1000')
# print(obj.__dict__)
print(obj.ram)
print(obj.storage)













        