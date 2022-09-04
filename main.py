#!/usr/bin/env python


# all about typer command line parser
# https://docs.python.org/3/library/argparse.html

import typer

# single argument
#def main(name: str): # arg name is type hinted to str
#    print(f"Hello there {name}!")

# double arguments
#def main(name: str, lastname: str): # arg name is type hinted to str
#    print(f"Hello there {name} {lastname}, how are  you!")
#if __name__ == "__main__":
#    typer.run(main)

# add one cli option --formal
#def main(name: str, lastname: str, formal: bool = False):
#    if formal:
#        print(f"Good day Miss {name} {lastname}.")
#    else:
#        print(f"Hello there {name} {lastname}.")
#
#if __name__ == "__main__":
#    typer.run(main)

# a cli option with a def value e.g. blank or no value for lastname
# use title Msr for combi of Miss and Sir aka gender-neutral title
def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname
    If --formal is used, say hi very formally complete with genderless title and titlecase
    """

    if formal:
        print(f"Good day Msr {name.title()} {lastname.title()}.")
    else:
        print(f"Hello there {name} {lastname}.")

if __name__ == "__main__":
    typer.run(main)