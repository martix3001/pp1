for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()
print("-------------------")
row = 6
while row > -1:
    col = 1
    while col < 4 :
        print(f" {row+col}",end='')
        col += 1
    print()    
    row -= 3    
