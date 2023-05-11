print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number(or q to quit): ")
    if first_number == "q" or not first_number or first_number.isdigit() == False:
        print("Invalid first input, goodbye for now!")
        break
    second_number = input("\nSecond number(or q to quit): ")
    if second_number == "q" or not second_number or second_number.isdigit() == False:
        # if second_number == 'q' or not second_number:
        # print("Bye")
        print("Invalid second input, goodbye for now!")
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(f"the answer is {answer}")

"""
pseudo code:
if input is q or Q, print bye
if input is empty, print bye
if input is not a digit, print bye
"""
