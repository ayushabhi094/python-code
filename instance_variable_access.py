class ExampleClass:
    def __init__(self, value):
        self.instance_variable = value

    def print_instance_variable(self):
        print(f"instance variable: {self.instance_variable}")

    def modify_instance_variable(self, new_value):
        self.instance_variable = new_value

obj = ExampleClass(15)
obj.print_instance_variable()
obj.modify_instance_variable(50)
obj.print_instance_variable()