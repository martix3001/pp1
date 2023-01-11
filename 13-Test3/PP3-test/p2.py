def f(c,r):
    count = 0
    max = r[1]
    min = r[0]
    for i in range(len(c)):
        if (c[i] >= min and c[i]<= max ):
            count += 1
    return count          