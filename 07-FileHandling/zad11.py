arr = ["film1","Film2","Film3","Film4","Film5"]
f = open("savingfile2.txt", "w")

for i in range(len(arr)):
    f.write(f"{arr[i]}\n")

f.close()