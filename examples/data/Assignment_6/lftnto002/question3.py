"""Program to count the number of votes for each political party in an election
   Bridgette Lefatsa
   LFTNTO002
   24 April  2014"""

#Heading
print("Independent Electoral Commission")
print("--------------------------------")
#Get vote list from user
votes=[]
vote=input("Enter the names of parties (terminated by DONE):\n")
while vote !="DONE":
    votes.append(vote)
    vote=input("")

#Get names of parties in elections
parties=[]
for x in votes:
    if x not in parties:
        parties.append(x)
parties.sort()

#Count votes
print("\nVote counts:")
for k in parties:
    count=0
    space_length= 11-len(k)
    for i in range(len(votes)):
        if votes[i]==k:
            count+=1
    print(k," "*space_length,"- ",count,sep="")