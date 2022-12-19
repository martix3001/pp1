import math
class Figures():

    @staticmethod
    def area_triangle(base,height):
        area = (base * height)/2
        return area
    @staticmethod
    def area_rectangle(side_a,side_b):
        area = side_a * side_b
        return area
    @staticmethod
    def area_circle(radius):
        area = round((radius**2)*math.pi,2)
        return area

print(Figures.area_triangle(6,2))
print(Figures.area_rectangle(4,7))
print(Figures.area_circle(3))