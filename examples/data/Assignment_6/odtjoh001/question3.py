"""Program to count the number of votes for a political party
John Odetokun ODTJOH001
20 April 2014"""
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
#initializing dictionary
nameDict = {}
name = input()
#adding names to list
while name != "DONE":
    if name not in nameDict:
        nameDict[name] = 1
    else:
        nameDict[name] +=1
    name = input()
print("\nVote counts:")
#print parties with set width of 10
for i in sorted(nameDict):
    print("{0:<10}".format(i) ,"-", nameDict[i])
    