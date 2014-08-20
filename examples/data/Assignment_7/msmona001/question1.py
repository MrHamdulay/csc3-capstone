"""List of strings without duplicates
Author: Onalerona Mosimege
30 April 2014"""

# A program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates

arrStrings = [] #Array for strings entered

#Enter strings till word is "DONE"
string = input("Enter strings (end with DONE):\n")
while string.upper() != "DONE":
    if not string in arrStrings:
        arrStrings.append(string)
    string= input("")

#print out unique list
print("\nUnique list:")
for i in range(len(arrStrings)):
        print(arrStrings[i])

