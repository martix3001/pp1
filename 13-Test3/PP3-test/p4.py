def f(d,n):
    odp = []
    for i in d.keys():
        if(d[f"{i}"] > n):
            odp.append(i)       
    o=""
    for i in range(len(odp)-1):
        o += f'{odp[i]},'
    if(len(odp)>0):
        o += f'{odp[-1]}'
    return o    