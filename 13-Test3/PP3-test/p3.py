def f(n):
    x = n.upper()
    if(n != x):
        return False
    if(n[0] != 'K'):    
        return False
    c = 0
    temp = 0
    for i in n:
        if ((i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0") and c >= 3):
            return False
        c += 1
        if((i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0" )):
            temp += 1
    if(temp < 3 or temp >5) :
            return False   
    return True            