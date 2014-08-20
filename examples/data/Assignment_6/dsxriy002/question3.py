#Riya Desai
#Assignment 6, Question 3
#23 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
partyname=input("Enter the names of parties (terminated by DONE):")

votes={}

while partyname !="DONE":
    if partyname in votes.keys():
        votes[partyname]+=1
    else:
        votes[partyname]=1
    partyname=input('')
print()
print("\nVote counts:")
for key in sorted(list(votes.keys())):
    print(key.ljust(10),"-",votes[key])