# class Vector:
#     def __init__(self, i ,j ,k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j+ {self.k}k"
    
#     def __add__(self,other):
#         return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
    
# obj1 = Vector(3,4,5)
# print(obj1)
# obj2 = Vector(6,7,8)
# print(obj2)
# obj3 = obj1 + obj2
# print(obj3)

class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"{self.p1} {self.p2}"

    def __add__(self, other):
        return Point(self.p1+other.p1, self.p2+other.p2)

p1 = Point(1,2)
print(p1)
p2 = Point(3,4)
print(p2) 
p3 = p1+p2
print(p3)











