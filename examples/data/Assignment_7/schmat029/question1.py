#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     prints out a list of unique strings
#
# Author:      Matthias
#
# Created:     27-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

string_list = []
print("Enter strings (end with DONE): \n")

while True:
    new_string = input()
    if new_string == "DONE":
        break
    elif new_string in string_list:
        # to prevent duplicates
        continue
    string_list.append(new_string)

print("Unique list:")

for s in string_list:
    print(s)

