list = [-15,8,-31,47,-2,19]
min = list[0]
max= list[0]

for i in list:
    if i < min:
        min = i
    if i > max:
        max = i
print(min," ",max)        