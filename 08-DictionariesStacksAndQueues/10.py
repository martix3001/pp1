arr = [{"country": "Poland", "population": 2352},
       {"country": "eng", "population": 525543},
       {"country": "eqwe", "population": 43245},
       {"country": "turtur", "population": 12341},
       {"country": "Puff", "population": 635247}]

c= 0
while c < len(arr):
    for key,value in arr[c].items():
        print(key,value,end=" ")
    print()    
    c+=1
     
