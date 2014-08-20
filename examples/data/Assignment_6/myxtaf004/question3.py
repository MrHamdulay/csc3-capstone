"""counts the number of votes for each political party in an election
Tafadzwa Moyo
21 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#Gets list of parties 
print("Enter the names of parties (terminated by DONE):")
a=input()
parlis=[]
while a!="DONE":
    parlis.append(a)
    a=input()

#Vote Count
votecount={}
for i in parlis:
    if i in votecount:
        votecount[i]+=1
    else: 
        votecount[i]=1

#Prints vote cont 
print()
print("Vote counts:")
for a in sorted(votecount.keys()):
    gap=10-len(a)
    print(a," "*gap," - ",votecount[a], sep="")
    