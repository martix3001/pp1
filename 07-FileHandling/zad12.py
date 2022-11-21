
f = open("shoppinglist.txt", "a")
product = input("Wprowadz pozycje do listy zakupow: ")
f.write(f"{product}\n")

f.close()