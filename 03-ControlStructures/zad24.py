x = int(input("How many stars at peak: ")) 
for i in range(x+1):
    for j in range(i):
        print("* ",end='')
    print()      
for i in range(x-1,0,-1):    
    for j in range(i):
        print("* ",end='')
    print()       
 