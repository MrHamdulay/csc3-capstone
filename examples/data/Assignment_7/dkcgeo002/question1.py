__author__ = 'George de Kock'
"""Program where the user can enter a list of strings and these strings
 are then printed in the same order but without duplicates.
 2014-04-27"""

unique = []
print("Enter strings (end with DONE):\n")
while True:
    item = input()
    if item == "DONE":
        break
    elif item not in unique:
        unique.append(item)

print("Unique list:")
for a in unique:
    print(a)