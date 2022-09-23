#!/usr/bin/env python

# this is my small script to ask user for todo note to input & append to the note.txt file
# so it will get appended IRT in the notes desklet of cinnamon DE

# define the target file, must be absolute
filename: str = "/home/erimendz/note.txt"



# add if name = main prelude
## read the whole file first
#with open(filename) as f:
#    print(f.read().strip("\n"))


# function add_todo
def add_todo():
    note_to_write = input("\nWhat todo task to add? ")
    if len(note_to_write) == 0:
        print("None given, try again next time :-) ")
        exit()
    # confirm to proceed
    confirm_msg = "Proceed to write [N/y]?"
    ask_confirm = input(confirm_msg)
    # if ['y', 'ye', 'yes', 'YES'] in ask_confirm:    # lol this is written backwards
    if ask_confirm in ["y", "ye", "yes", "YES"]:
        # if yes, make upper case and write, else discard silently
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
        print("Do delete function")

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

"""
