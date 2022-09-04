#!/usr/bin/env python


# all about typer command line parser
# https://docs.python.org/3/library/argparse.html

import typer

def main(name: str): # arg name is type hinted to str
    print(f"Hello there {name}!")

if __name__ == "__main__":
    typer.run(main)

