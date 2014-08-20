"""Count votes for election
Paul Truter
22 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#get list of names
names = []
name = input("Enter the names of parties (terminated by DONE):\n")
while name != "DONE":
    names.append(name)
    name = input("")
print()

#sort list in alphabetical order
names.sort()
 
print("Vote counts:")
#count number of occurences]
newlist=[]
for name in names:
    if name in newlist:
        continue
    else:
        print( ("{0:<10}").format(name),"-",names.count(name) )
        newlist.append(name)