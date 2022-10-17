from random import randrange
sum = 0
for i in range(0,3): 
    x = randrange(0,6)
    print(x)
    sum = sum + x
print(f"Sum {sum}")    