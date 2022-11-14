list = [1,2,3,4,5]
print(list)
list[0] = list[0]-1
print("a.",list)
list[len(list)-1] += 4
print("b.",list)
list[int(len(list)/2)] *= 2
print("c.",list)
for i in range(len(list)):
    list[i]+=1
print("d.",list)    