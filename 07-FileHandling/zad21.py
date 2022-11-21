file = open('zad21.txt','w')
for i in range(1,11):
    file.write(f"{i},{i*i},{i*i*i}\n")

file.close()    