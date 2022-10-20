def prime(n):
    for i in range(2,n):
        if n % i == 0:
           return False
    return True              
N = int(input("N leading prime numbers: "))

i = 2
while N > 0:
    if(prime(i)):
        print(f"{i}",end=' ')
        N -= 1
    i += 1 