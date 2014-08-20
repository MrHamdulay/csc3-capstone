# Assignment 6 - Question 1
# A program that prompts the user to enter a list of strings and then prints the list right aligned
# Written by: Laene van Niekerk 
# VNKLAE001

list = []   # Start with an empty list

new_item = input("Enter strings (end with DONE):\n")    # Get the first item from the user

while new_item != "DONE":   # While loop that gets more items from the user until the sentinel is entered
    list.append(new_item)   # Adds item to the list
    new_item = input("")    # Enables user to enter new item
    
print()
print("Right-aligned list:")

max = 0
for i in list:              # Checks to see which word in the list is the longest
    string_len = len(i)
    if string_len > max:
        max = string_len
    else:
        max = max

for word in list:           # Prints out the list line by line right justified to the length of the longest word
    print(word.rjust(max))