# Find unique string in a list of strings
# Conor O'Sullivan
# 27/04/2014
"""Write a Python program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.

Use the sentinel "DONE" to end the input list.

Sample I/O:


the
old
man
and
the
sea
DONE


the
old
man
and
sea"""

#Enter strings and obtain unique words
enter = input("Enter strings (end with DONE):\n")
unique = []
while enter != "DONE":
       if enter not in unique: 
              unique.append(enter)
       enter = input("")
       
#Print unique words
print("\nUnique list:")
for word in unique: 
       print(word)