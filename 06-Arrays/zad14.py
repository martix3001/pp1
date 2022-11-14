arr = [[True,False],[True,True],[False,False]]
print(arr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (arr[i][j] == False):
            arr[i][j] = True
        if (arr[i][j] == True):
            arr[i][j] = False   

print(arr)           