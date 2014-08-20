"""Nicholas Stephenson
Program to create a list of unique words from an inputted list"""

#The folllowing is required to add the given strings into the list
strings = ""
listofstrings= []
print("Enter strings (end with DONE):")
while strings != "DONE":
    strings = input()
    listofstrings.append(strings)
listofstrings.pop()

singlelist = []
for i in listofstrings:
    if i not in singlelist:
        singlelist.append(i)

print("")
print("Unique list:")
for j in singlelist: print(j)
    