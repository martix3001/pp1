n = 50

n1 = 0
n2 = 1

count = 0

#if n == 1:
#   print("Fibonacci sequence up to",n,":")
#   print(n1)
#else:
print("Fibonacci sequence:")
while count < n:
       print(n1,end=' ')
       temp = n1 + n2 
       n1 = n2
       n2 = temp
       count += 1