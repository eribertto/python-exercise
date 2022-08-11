#!/usr/bin/env python

# Starting code for Level 2 Treasure Island project

# This project will ask the user a series of questions as they navigate through a treasure island. However, if they make the wrong decision, they will meet an untimely end!

# ASCII art to display to user
ASCII_ART = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

# 1. Print the ASCII_ART variable
print(ASCII_ART)

# 2. Print an introduction message to the user
print("You are exploring a rainforest in hunt for treasure")
print("Legend has it that there is some buried on a nearby island")

# 3. Finish the rest of the program using what you've learnt about if statements
swim_or_wait = input(
    "You come to a lake. Do you either want to wait for a boat, or swim across? (swim/wait): "
)

if swim_or_wait == "swim":
    print("You get eaten by a hungry shark. Game over.")

print("A boat arrives and you arrive at the island safely.")

cave_or_stay = input(
    "You come to a cave, do you want to venture inside or walk on? (venture/walk)"
)
if cave_or_stay == "venture":
    print("You are squished by boulders never to be seen again.")
elif cave_or_stay == "walk":
    crossroad_turn = input(
        "You're at a crossroads. Do you want to go left, right or straight? (left/right/straight):"
    )
    if crossroad_turn == "left":
        print("You are trampled by a herd of wildebeest, game over.")
    elif crossroad_turn == "straight":
        print("You get stung by a poisonous wasp, game over.")
    elif crossroad_turn == "right":
        print("You march on and find the treasure, wahoo!")
else:
    print("Make sure you enter swim/wait... game over!")
