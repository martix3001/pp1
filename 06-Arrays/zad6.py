 
list = [2,3,7,5,4]

print("a.",list)
print("b.",len(list))
print("c.",list[0])
print("d.",list[1])
print("e.",list[len(list)-1])
print("f.",list[len(list)-2])
print("g.",list[0]+list[len(list)-1])
print("h.",list[int(len(list)/2)])
print('i. ',end='')
for i in range(len(list)):
    print(list[i],' ',end='')
print()
print('j. ',end='')
for i in range(int(len(list)/2),len(list)):
    print(list[i],' ',end='')