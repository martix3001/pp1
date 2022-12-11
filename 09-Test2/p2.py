def f(human_age):
    age = 0
    if (human_age == 1):
        return 10
    if (human_age == 2): 
        return 20       
    
    for i in range(human_age-2):
        age += 4
    age += 20

    return age    

print(f(12))
print(f(2))