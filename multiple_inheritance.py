class Base1:
    def details(self):
        print("this is base class 1")
class Base2:
    def second_details(self):
        print("this is base class 2")

class Base3(Base1, Base2):
    def last_details(self):
        print("this is multiple inheritance")

obj = Base3()
obj.last_details()
obj.second_details()
obj.details()