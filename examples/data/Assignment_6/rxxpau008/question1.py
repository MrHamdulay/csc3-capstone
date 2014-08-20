#Description: Aligns a list of strings to the right
#Name: Paul Roux - RXXPAU008
#Date: 22 April 2014

names = []
max_length = 0

entry = input("Enter strings (end with DONE):\n")
while entry != "DONE": #Used to capture stringss until "DONE" is entered
    names.append(entry)
    entry = input()

for i in names: #Used to find the longest string
    name_length = len(i)
    if name_length > max_length:
        max_length = name_length
print()
print("Right-aligned list:")
for i in names: #Prints out the strings, aligned to the right
    print(' '*(max_length-len(i))+i)