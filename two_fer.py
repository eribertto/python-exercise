def two_fer(name="you"):
    result = print(f"One for {name}, one for me.\n")
    return result

two_fer()



ask_number = input("Please enter your name: ")
if not ask_number:
    print("One for you, one for me.")
else:
    print(f"One for {ask_number}, one for me.")
    
# another solution using a function
