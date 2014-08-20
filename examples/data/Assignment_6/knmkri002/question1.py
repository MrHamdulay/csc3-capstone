"""program to create a list of names entered by the user and right aligned
 Kristin Kinmont
 20 April 2014"""

#create an empty list
names = []

#get a list of names
name = input("Enter strings (end with DONE):\n")
while name != "DONE":
    names.append(name)
    name = input("")

#find longest name
length = 0
for i in names:
    if length < len(i):
        length = len(i)
print()

#right align the names
print("Right-aligned list:")
for i in names:
    spaces = length - len(i)
    print(" "*(spaces)+i)
