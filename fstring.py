import datetime

name = "Eriberto"
age = 55
anniversary = datetime.date(2000, 5, 22)
print(f"My name is {name}, my age next year is {age+1}, my anniversary is {anniversary: %A, %B %d, %Y}.")
