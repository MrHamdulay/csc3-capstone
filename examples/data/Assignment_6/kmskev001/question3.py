"""program to count the number of votes for each political party
   kevin kumasamba
   22 april 2014"""


print("Independent Electoral Commission")
print("--------------------------------")

parties=[]
names=input("Enter the names of parties (terminated by DONE):\n")
while names!="DONE":
    parties.append(names)
    names=input("")
    
# to work out the vote counts, program must be created that counts the occurence of each item in the list

print("\nVote counts:")

# need to print the item and the number of times it appeared in list - check for each item in the list if it appears more than once
# print item and the number of times it appeared
# if item appears more than once, do not print item
# parties must be sorted in alpha order
parties.sort()
party_vote=[]
# make a 2d list containing the party and the number of votes
for party in parties:
    votes=parties.count(party)
    party_vote.append([party, votes])
for pv in party_vote:
    if pv==pv:
        num=party_vote.count(pv)
        for i in range(num-1):
            party_vote.remove(pv) # it works :D
            
# print out the party and the votes next to each other
for both in party_vote:
    count=0
    for each in both:
        if count==0:
            print(each, end="")
            count+=1
            length=len(each)
        else:
            if length==10:
                print("{0:>{1}}".format(" ", 10-length), "- ", each, sep="")
            else:
                print("{0:>{1}}".format(" ", 10-length), " - ", each, sep="")
     
            

    
    
    
    




    

    
    
    
    

    