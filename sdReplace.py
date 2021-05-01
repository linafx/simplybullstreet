""" replace all single quotes in a string with double quotes """

import sys

nav = ""

for c in sys.argv[1]:
    if c == "'":
        nav += '"'
    else:
        nav += c

print(nav)
