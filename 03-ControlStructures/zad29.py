
sum=0
mean=0
add=0

while True:
    x=int(input("Enter numer: "))
    if x == 0:
        break
    else:
        sum += x
        add += 1
mean = round(sum/add,2)        
print(f"RESULT: Quantity={add}, Sum={sum}, Mean={mean}")        