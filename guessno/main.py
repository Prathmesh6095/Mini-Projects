import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f"Guess a nnumber between 1 and {x}")
        if guess < random_number:
            print('Sorry! guess again')