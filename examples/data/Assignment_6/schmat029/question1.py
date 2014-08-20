#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     printing out a list of elements that are right-aligned
#
# Author:      Matthias
#
# Created:     19-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list = []
max_string = ""

print("Enter strings (end with DONE):")
print("")

# create list
while True:
    string = input("")
    if string == "DONE":
        break
    list.append(string)

# check for longest string in list
for word in list:
    if len(word) > len(max_string):
        max_string = word

# print indented elements of list
print("Right-aligned list:")
for s in list:
    print("{0:>{1}}".format(s,len(max_string)))