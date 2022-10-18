human_years = int(input("Enter the dog's age in human years: "))
dog_years = 0

while human_years > 2:
    x = human_years-2
    for i in range(x):
        dog_years = dog_years + 4
    human_years = 2
for i in range(human_years):
    dog_years = dog_years + 10.5        
print("The dog's age in dog’s years is",dog_years,"years")

    
