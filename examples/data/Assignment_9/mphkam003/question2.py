"""progam to change the format of file
Kamogelo Mphela
11 may 2014"""

import sys
sys.setrecursionlimit (3000)
input_file= input("Enter the input filename:\n")
output_file = input ("Enter the output filename:\n")
line_width = eval(input ("Enter the line width:\n"))

k = open(input_file,"r")
strings = k.readlines()
k.close()
stuff = ""
for string in strings:
    stuff += string + " "

# remove "\n" and extra spacing from the old string
s = stuff.find("\n")
stuff = stuff.replace(stuff[s],"")


def F_string(stuff):
    """return the string formatted to the desired length per line"""
    if len(stuff) < line_width:
        return stuff
    elif stuff[line_width] == " ":
        return stuff[:line_width] + "\n" + F_string(stuff[line_width+1:])
    else:
        temp = stuff[:line_width]
        cut = temp.rfind(" ")
        return stuff[:cut] + "\n"+ F_string(stuff[cut+1:])
    
x = F_string(stuff)
f = open(output_file, "w")
print (x, file = f)
f.close()