#!/usr/bin/env python


# Bro Code Python course
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# all about loop controls in Python

# break - used to terminate the loop entirely
# continue - skips to the next iteration of the loop
# pass - does nothing, acts like a placeholder

# break
#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break
#print(f'Hello there {name}')
#
## continue
#phone_number = "123-456-789"
#print(f'Old number is {phone_number}')
#for i in phone_number:
#    # skip the dash symbol
#    if i == "-":
#        continue
#    print(i, end="")

# pass 
print('Using pass in a for loop')
for i in range(1, 21):
    # skip unlucky number 13
    if i == 13:
        print(f'skipping unlucky {i}!')
        pass
    else:
        print(i)