print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number(or q to quit): ")
    if first_number == 'q' or not first_number:
        break
    second_number = input("\nSecond number(or q to quit): ")
    if second_number == 'q' or not second_number:
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
