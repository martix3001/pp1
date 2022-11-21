import random

file = open('randomnumbers.txt','w')
for i in range(50):
    x = random.randrange(100,999)
    file.write(f"{x}\n")