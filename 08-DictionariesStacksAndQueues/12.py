import json
books = {
    "name": "WayofSzaman",
    "yearofpub": 2020,
    "numberofpag": 250,
    "author": "mahanienko",
    "ongoing": False,
}

file = open("favourite.json","w")
file.write(json.dumps(books,indent = 4))
