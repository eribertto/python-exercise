#!/usr/bin/env python

# remove spaces from filenamenamename names
# https://stackoverflow.com/questions/12314285/how-do-i-remove-spaces-from-all-the-filename-names-in-the-current-directory

import os

print("This script will strips spaces from filemes in the current directory")


def main():
    for filename in os.listdir("."):
        print(f"before {filename}")
        rem_space = filename.replace(" ", "_")  # replace space with underscore
        # print(rem_space)
        if rem_space != filename:
            os.rename(filename, rem_space)  # from, to
            print(f"after {rem_space}")


if __name__ == "__main__":
    main()
