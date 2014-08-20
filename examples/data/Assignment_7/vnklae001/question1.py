# Assignment 7 - Question 1
# A program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates
# Written by: Laene van Niekerk
# VNKLAE001

lis = []    # Start with an empty list
add_list = input("Enter strings (end with DONE):\n")   # Gets input from the user

while add_list != "DONE":   # Continues to get input from the user until they enter "DONE"
    lis.append(add_list)
    add_list = input("")
    
print()

no_duplicate_list = []  # Start with an empty list to create new list with no duplicates

for word in lis:    # Checks to see if the word is already in the list
    if word not in no_duplicate_list:
        no_duplicate_list.append(word)
        
print("Unique list:")

for word in no_duplicate_list:  # Prints the list excluding the duplicates
    print(word)