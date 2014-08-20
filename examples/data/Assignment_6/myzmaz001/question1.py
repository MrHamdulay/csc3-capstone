""" Program to print out an alligned list of strings entered by user
Mazwi Myeza
21 April 2014
Assignment6
Question1
"""
# setting up a loop counter variable, asking for user input of strings after setting up an array 
counter = 0
strings = []
name = input("Enter strings (end with DONE):\n")
#Loop to store strings in the array
while name != 'DONE':
    strings.append(name)
    counter += 1
    name = input()
#loop to get the longest string
max = 0
for i in range(counter):
    x = len(strings[i])
    if x > max:
        max = x
#printing out right-alligned list using loop, after printing out title      
print()
print("Right-aligned list:")
for k in range (len(strings)):
    space = max - len(strings[k])
    print(space*" ",strings[k], sep = "")

    