def f(arr):
    if(len(arr) != len(arr[0])):
        return False
    for i in range(len(arr)):  
        for j in range(len(arr[i])):
            if (i+1) * (j+1) != arr[i][j]:
                return False
    return True

print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))