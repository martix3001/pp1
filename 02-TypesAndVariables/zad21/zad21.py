from random import randrange
answer = randrange(0,6)
guess = -1
while guess != answer:
    print("Try again")
    guess = int(input("Your guess: "))

print("True")    