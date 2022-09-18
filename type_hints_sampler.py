#!/usr/bin/env python

# all about type hints in Python
# https://fastapi.tiangolo.com/python-types/

# type hints for string variables in the func definition
def get_full_name(first_name: str, last_name: str):
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

# call the function
print('Hello there ', (get_full_name('james', 'bond 007')))