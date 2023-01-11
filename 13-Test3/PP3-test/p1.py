def f(n):
    odp = ""
    while n - 100 >= 0:
        odp += "*"
        n -= 100
    while n - 10 >= 0:    
        odp += "+"
        n -= 10
    while n - 1 >= 0:
        odp += "/"
        n -= 1
    return odp             