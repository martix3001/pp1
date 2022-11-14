list = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max = ''
maxlen = 0
for i in range(len(list)):
    if len(list[i]) > maxlen:
        max = list[i]
        maxlen = len(list[i])
print("Longest name: ",max)