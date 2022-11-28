person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
#a
print("a: ",person)
#b
print("b: ",person["name"])
#c
print("c: ",person["hobby"])
#d
person.update({"surname":"Nowak"})
print("d: ",person["surname"])
#e
person.update({"married":False})
print("e: ",person["married"])
#f
person["gender"] =  "male"
print("f: ",person)
#g
person["hobby"].append("bicycle")
print("g: ",person)
#h
person["phone"]["work"] = "313131444"
print("h: ",person)