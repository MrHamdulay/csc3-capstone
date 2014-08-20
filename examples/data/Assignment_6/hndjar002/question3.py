""" Program to count the number of votes in a political party election (Question 3)
Jaren Hendricks
24 April 2014"""

# Empty dictionaries/lists 
SetParties = {}
Names = []
newSet = []

# Headings
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

# Adds strings to lists and breaks when user enters 'DONE'
while True:
    n = input()
    if n == "DONE":
        break
    else:
        Names.append(n)
        
        # Removes duplicate values and sorts the parties alphabetically 
        SetParties = set(Names)
        newSet = sorted(SetParties)

# Prints space and a heading
print()
print("Vote counts:")

# Counts the numbers of votes and displays output in a formated style
for i in newSet:
    count = Names.count(i)
    print('{0:<10}'.format(i), "-", count)
