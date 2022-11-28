import json

with open("data.json") as file:
    data = json.load(file)

c= 0
while c < len(data):

    for k,v in data[c].items():
        print(k,":",v)
    c+=1
    

