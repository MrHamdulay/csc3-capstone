""" a Python program where the user can enter a list of strings and these 
strings are then printed in the same order but without duplicates.
Author: Dominic Manthoko
27 April 2014
"""

# prompt the user for input
string = input("Enter strings (end with DONE): \n")

# create an empty list
string_count = []

while string != 'DONE':
    # add the string to string count only if it has not been typed yet
    if string not in string_count:
        string_count.append(string)
    
    # prompt the user to enter another string    
    string = input("")
    
print("\nUnique list:")
# print each unique item in the list on a new line
for i in range(len(string_count)):
    print(string_count[i])