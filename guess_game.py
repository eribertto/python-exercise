#!/usr/bin/env python


# guessing game
# exercise 1 Python Workout by the author


import random

def guessing_game():
    #method randint begins 0-99 excluding 100
    answer = random.randint(0, 100)
    while True:
        user_guess = int(input('What is your guess? (numbers only)') )
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess {user_guess} is too low!')
        else:
            print(f'Your guess {user_guess} is too high')

guessing_game()