# Matthew Finlayson - FNLMAT001
# Assignment 7 question 1
# 01/05/14

# user enters a list of strings and the strings are then printed out in the same order but without duplicates

strings = []
s = input("Enter strings (end with DONE):\n")
while s!= "DONE":
    if not(s in strings):
        strings.append(s)
    s = input()

print()

print("Unique list:")
for i in range (len(strings)):
    print(strings[i])