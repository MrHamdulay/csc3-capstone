#Kalind Ramnarayan
#23 April 2014
#voting simulation

print("Independent Electoral Commission")
print("--------------------------------")

votelist=[]                                            #Create a list
string=input("Enter the names of parties (terminated by DONE):\n")
while string!="DONE":                               # add strings to the list
    votelist.append(string)
    string=input()
    
partylist=[]

for i in votelist:
    if not i in partylist:
        partylist.append(i)
    
x=partylist.sort()

print()
print("Vote counts:")
gap=" "
for i in partylist :
    print(i,gap*(9-len(i)),"-",votelist.count(i))
