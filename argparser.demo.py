#!/usr/bin/env python


# argparse - Parser for command line options & arguments
# https://docs.python.org/3/library/argparse.html

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.accumulate(args.integers))

# to run this program get python to call this script and provide arguments