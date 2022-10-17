import math


a = float(input("Lenght a: "))
b = float(input("Lenght b: "))
c = float(input("Lenght c: "))

s= (a+b+c/2)
area = math.sqrt(s*(s - a)*(s - b)*(s - c))
print(area)