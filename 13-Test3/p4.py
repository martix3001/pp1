def f(d):
    cars = []
    for data in d:
        if data[1] == "in":
            cars.append(data[0])
        else:
            for i in range(len(cars)):
                if  data[0] == cars[i] :
                    cars.pop(i)
                    break    
    cars.sort()            
    return cars

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))