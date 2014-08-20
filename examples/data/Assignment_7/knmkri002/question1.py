"""Program to remove duplicate strings from a given list
Kristin Kinmont
27 April 2014"""

# Get a list of strings from the user and creat a list
string = input("Enter strings (end with DONE):\n")
strings = []
while string != "DONE":
    strings.append(string)
    string = input("")
print()
# create a new list without duplicates
strings_new = []
for i in strings:
    if i not in strings_new:
        strings_new.append(i)
# print new list
print("Unique list:")
for i in strings_new:
    print(i)
    

    