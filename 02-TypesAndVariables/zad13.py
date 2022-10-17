import math
#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
radius = int(input("Input radius of the circle: "))
stable = math.pi

# calculate area 
area = round(stable*radius*radius,2)

# calculate circumference 
cir = round(2*stable*radius,2)

# display results 
print(f"radius is {radius} and area is {area} and circumference  {cir}")
