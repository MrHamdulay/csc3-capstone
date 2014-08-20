'''program to count the number of votes for each political party in an election
Michele Balestra  BLSMIC004
23 April 2014'''

print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
names = ''
listNames = []

# adds each string to a list
while names != "DONE":
    names = input()
    listNames.append(names)

# creates a new list made of each unique string in listNames
newList = []
for item in listNames:
    if (item not in newList) and (item != 'DONE'):
        newList.append(item)
       
# sorts and displays number of each unique string 
newList.sort()
print('\nVote counts:')
for i in range(len(newList)):
    print(newList[i].ljust(10), '-'.rjust(0), str(listNames.count(newList[i])))