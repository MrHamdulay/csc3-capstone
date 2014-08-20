''' program where user enters list of strings followed by sentinel "DONE" is then printed out right-aligned with the longest string
Michele Balestra    BLSMIC004
23 April 2014'''

print("Enter strings (end with DONE):")
listNames = []
names = ' ' 
max = 0

# adds each string to a list
while names != 'DONE':
    names = input()
    listNames.append(names)

# determines length of longest string in list
for item in listNames:
    if len(item)>max:
        max = len(item)

# prints right-aligned list
print("\nRight-aligned list:")
for j in range(len(listNames)-1):
    print (listNames[j].rjust(max))
    