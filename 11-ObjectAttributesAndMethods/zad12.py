import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        if((self.x == other.x) and (self.y == other.y) ):
            return 0
        else:
            dis = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 )
            return dis 
        
p1 = Point(5,0)
p2 = Point(8,0)
p3 = Point(5,0)

print(p1==p2)
print(p1==p3)