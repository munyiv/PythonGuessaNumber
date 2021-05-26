import random
num=random.randrange(1,50)
guess=int(input("Take a wild guess between 1 and 50:"))
while guess != num:
    if guess < num:
        print("\n You need to guess a little higher.Try again")
        guess=int(input("Take a wild guess between 1 and 50:"))
    else:
        print("You need to guess lower.Try again")
        guess=int(input("Take a wild guess between 1 and 50:"))
print("Hurray! You guessed the number correctly Congrats")