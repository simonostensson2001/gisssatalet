import random
loop = True
number = random.randint(1, 10)
while loop == True:
    guess = int(input("Gissa en siffra mellan 1-10: "))
    print
    if guess < number:
        print("för lågt. Gissa igen:  ")
    elif guess > number:
        print("För högt. Gissa igen:  ")
    else:
        print("Du gissade rätt")
        loop = False
