# Matthew Finlayson - FNLMAT001 
# Assignment 6 question 1
# 22/04/14

# asks the user to input a length of strings and stores the strings in an ever-expanding list until the user enters "DONE"
s = input("Enter strings (end with DONE):\n")
strings = []
maxLength = 0 # keeps track of the longest word stored
while s != "DONE":
    strings.append(s) # adds each new string onto the strings list
    if (len(s)>maxLength): # checking to see if the new word is longer 
        maxLength = len(s)
    s = input("") # repromts user for input

print()

print("Right-aligned list:")
for i in range(len(strings)):
    length = len(strings[i])
    print(" "*(maxLength-length)+strings[i]) # makes sure all the strings are right-aligned

