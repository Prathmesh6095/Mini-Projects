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
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low(L), or correct (c)??")
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    
    print(f"Yayy! The computer guessed your number {guess}, correctly!")