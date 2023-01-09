def f(n):
    answear = ""
    if(n <= 0):
        return answear
    for i in range(1,n+1,1):
        answear += "/"
        if(i % 5 == 0 and i != n):
            answear += "-"
    return answear

print(f(-4))  
print(f(0))    
print(f(5))    
print(f(7))    
print(f(10))    
print(f(36))          