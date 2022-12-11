def f(array2D):
    sum = [0]*len(array2D[0])
    for row in range(len(array2D)):
        for col in range(len(array2D[row])):
            sum[col]+= array2D[row][col]

    return sum

arr =[ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]
print(f(arr))