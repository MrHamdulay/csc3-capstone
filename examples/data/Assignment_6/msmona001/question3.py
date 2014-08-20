#program to count the number of votes for each political party in an election.

#print title
print("Independent Electoral Commission\n--------------------------------")

arrParties =[]
#Enter all parties till word is "DONE"
party = input("Enter the names of parties (terminated by DONE):\n")
while party.upper() != "DONE":
    arrParties.append(party)
    party= input("")

ArrDic= {}
# count party votes and add new as encountered
for party in arrParties:
    i=0
    if not party in ArrDic:
        ArrDic[party] = 1
    else:
        ArrDic[party] += 1
    i+=1
NewArr=list(ArrDic)
NewArr.sort()

#print out votes
a= "{0:<10}"
print("\nVote counts:")
for i in NewArr:
        print(a.format(i),'-',ArrDic[i])
