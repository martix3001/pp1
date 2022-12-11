def f(dictionary,x,y):
    min = x
    max = y
    sum = 0 
    for key,value in dictionary.items():
        for i in range(len(value)):
            if (value[i] >= min) and ( value[i] <= max):
                sum += value[i]
    return sum      

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))        
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10)) 