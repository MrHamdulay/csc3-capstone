"""question1.py Program to remove duplicated strings in a list
Author : Musa Xakaza
Date : 27/04/2014"""

values = []
#get unique values and store them in the list, using the sentinel "DONE" to end the input list.
value = input("Enter strings (end with DONE):\n")
while value != "DONE":
    if not value in values:
        values.append(value)
    value = input()

#print values in the same order without duplicates.
print("\nUnique list:")
for value in values:
    print(value)