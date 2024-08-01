class MyClass:
    def __init__(self, v):
        self.value = v

    # def show(self):
    #     print(f"hello this is value {self.value}")
    
    def set_value(self, n):
        self.value = n

    def get_value(self):
        print(10*self.value)

obj = MyClass(10)
# obj.show()
obj.set_value(20)
obj.get_value()