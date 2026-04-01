import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a nnumber between 1 and {x} "))
        if guess < random_number:
            print('Sorry! guess again. Too low');
        elif guess > random_number:
            print('Sorry! guess again. Too big')

    print(f"Yay, Congrats! you guessed the {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
 
    
    print(f"Yayy! The computer guessed your number {guess}, correctly!")