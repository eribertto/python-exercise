#!/usr/bin/env python

# this is my small script to ask user for todo note to input & append to the note.txt file
# so it will get appended IRT in the notes desklet of cinnamon DE

# define the target file, must be absolute
filename: str = "/home/erimendz/note.txt"
#note_to_write = input("\nWhat todo task to add? ")
confirm_msg = "Proceed [N/y]?"

def check_empty_input():
    note_to_write = input("\nWhat todo task to add? ")
    if len(note_to_write) == 0:
        print("None given, try again next time :-) ")
        exit()
    
# function add_todo
def add_todo():
    #note_to_write = input("\nWhat todo task to add? ")
    print(("You selected Add"))
    check_empty_input()
    ask_confirm = input(confirm_msg)
    if ask_confirm in ["y", "Y"]:
        note_to_write = note_to_write.upper()
        with open(filename, "a") as f:
            f.write("\n===||===\n")  # make this a function
            f.write(note_to_write)
    else:
        print("Bye!")

def get_choice():
    choice = input("[A]dd or [D]elete todo? ")
    if choice in ["a", "A"]:
        add_todo()
    elif choice in ["d", "D"]:
        del_todo()

# function delete_todo
def del_todo():
    print(("You selected Delete"))
    line_to_delete = input("What todo task to delete? ")
    breakpoint()
    with open(filename) as f:
        lines = f.readlines()       # this is a list
    with open(filename, "w") as f:
        for line in lines:
            if line.strip("\n").lower() != line_to_delete.lower():
                f.write(line)
                
        #print(type(lines))
#       for line in f:
#           if line_to_delete.lower()  in line.lower():
#               print("This line will be deleted: ", line)
#               line.
#               print("Done")

get_choice()

"""
feature enhancements:
1. make this executable to be available in user environment
2. ask user if to add or delete todos in existing file
3. create add and delete functions
4. for delete function ask what line/lines to delete (you can visually see in the applet)
    tip: use module re
5. for add function use the above
6. save working file in python-exercise repo
7. add name = main prelude

NB: for tabular format aka to use free space of desket
consider using bash column command
or is there an equivalent in python for tabular style write formatting

# add if name = main prelude
## read the whole file first
#with open(filename) as f:
#    print(f.read().strip("\n"))
"""
