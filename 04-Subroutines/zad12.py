
def sum(N):
    if N != 0:
        return N + sum(N-1)
    else:
        return N       


print(sum(2))           


