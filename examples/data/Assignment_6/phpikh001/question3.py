#Ikhlaas Pohplonker
#23 April 2014
#a program to count the number of votes for each political party in an election
print("Independent Electoral Commission")
print("--------------------------------")
names=input("Enter the names of parties (terminated by DONE):\n")
counters={}#dictionary with no items
while names != "DONE":#asks user to enter a name of the party until DONE is entered
    if not names in counters:
            counters[names]=0#adds new item to dicitonary
    counters[names]=counters[names]+1    
    names = input()
grid=[]#empty list
for i in counters:
    grid.append(i)#adds key in dictionary to grid
grid.sort()#sorts items in grid into alphabetical order
print()
print("Vote counts:")
for name in grid:
    z = ("{0:<10}").format(name)
    print(z,"-",counters[name])