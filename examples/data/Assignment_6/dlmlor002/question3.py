"""program to count votes for political parties
Lorena Dal Maso
23 April 2014"""

print("Independent Electoral Commission\n--------------------------------")

print("Enter the names of parties (terminated by DONE):")

candidates=[]

#create list of parties
party=input("")
party_list=[party]
while party !="DONE":
        if party=="DONE":
                break
        party=input("")
        if party!="DONE":
                party_list.append(party)
                if party not in candidates:
                        candidates.append(party)
        
candidates.sort()                

print()
print("Vote counts:")
width2=10

for i in range(len(candidates)):
        print(candidates[i]," "*(width2-len(candidates[i])+1),"- ",party_list.count(candidates[i]),sep="")
