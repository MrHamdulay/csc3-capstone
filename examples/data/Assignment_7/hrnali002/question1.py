"""A program to print a list with not duplicated words
Alison Hoernle
HRNALI002
27 April 2014"""

# get input and convert to a list
list = []
strings = input("Enter strings (end with DONE):\n")

while strings != "DONE":
    list.append(strings)
    strings = input()

print()    
print("Unique list:")

# create an empty string and then go through list. Add each word to empty string and if in string already then don't print that word again
counted_words = ''
for string in list:
    if string in counted_words:
        continue
    else:
        print(string)
        counted_words += string