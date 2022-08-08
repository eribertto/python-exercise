#!/usr/bin/env python

# see notes on the side bar
# exercise 5 Python Workout by the author

def pig_latin(word):
    if word[0] in 'aeiou':
        # add way to the word
        return f'{word}way'
    # else
    # return the word but move the first char to the last then add 'ay'
    return f'{word[1:]}{word[0]}ay'

myword = 'abracadabra'
print(f'the word is {myword}')
print('the result is:', pig_latin(myword))
#print(pig_latin(myword))
# NB: upload the practice scripts to github so all machines can make use of
# Code editor is Thonny in Fedora36 box