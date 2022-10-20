a = 4
b = 15

for i in range(1,a+1,1):
    if( i == 1 or i == a):
        for j in range(b):
            print("*",end='')
        print()  
    else:
        print("*",end='')
        for j in range(b-2):
            print(" ",end='')
        print("*",end='')   
        print()      
