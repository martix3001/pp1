x = input("Name the file: ")
file = open(x,'r')
sum = 0
for line in file:
     sum += 1

print("File name: ",x)
print("Number of lines: ",sum)


