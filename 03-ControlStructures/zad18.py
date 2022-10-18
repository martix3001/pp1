from multiprocessing import current_process


amount = int(input("Enter the amount in PLN: "))
curr = [5,2,1]
curr_ile = [0,0,0]
n=0
while amount!= 0:
    if amount-curr[n] >= 0:
        amount = amount-curr[n]
        curr_ile[n] += 1
    else:
        n += 1

print(f"5 zł- {curr_ile[0]}")
print(f"2 zł- {curr_ile[1]}")
print(f"1 zł- {curr_ile[2]}")
