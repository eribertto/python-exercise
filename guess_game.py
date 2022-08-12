#!/usr/bin/env python


# guessing game
# exercise 1 Python Workout by the author


import random


def guessing_game():
    # method randint begins 0-99 excluding 100
    answer = random.randint(1, 101)
    while True:
        #user_guess = int(input('What is your guess? (numbers only) '))
        user_guess = (input('What is your guess? (numbers only) '))
        if not user_guess.isdigit():
            print("Only digit numbers are allowed. Try again!")
            break
        user_guess = int(user_guess)
        if user_guess > 100:
            print('Max number allowed is up to 100 only')
            break
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess {user_guess} is too low!')
        else:
            print(f'Your guess {user_guess} is too high')


guessing_game()
# todo: sanitize for user inputs that are not numbers
# todo: also guard for inputs over 100
