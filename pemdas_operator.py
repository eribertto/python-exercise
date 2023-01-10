# PEMDASLeR math operator precedence in Python
# Parens, Exponent, Multiply, Division, Add, Subtract and operation from Left to Right
# note division yields a floating point number result
msg = "The arithmetic result is: "
print(f'{msg}', 3*3+3/3-3)

'''order of precedence as follows
multiply 3*3
division 3/3 note this gives you float
addition: multiply result + div result
subtraction: add result subtracted by 3
'''