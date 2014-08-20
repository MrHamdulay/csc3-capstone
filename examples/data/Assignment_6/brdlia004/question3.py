"""Vote Counter"""
#Liam brodie
#BRDLIA004
#4.21 2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
print()

partylist=[]
partydic = {}
i=""
while i != "DONE":
    i = input("")
    partylist.append(i)
    partylist = sorted(partylist)
    partydic[i] = i
        
#del partylist[-1]
partylist = sorted(partylist)
#partydic = sorted(partydic.keys())

del partydic["DONE"]

print("Vote counts:")
for j in sorted(partydic.keys()):
    print(j," "*(9-len(j)), "-", partylist.count(j))
