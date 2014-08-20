"""Tevin Chetty
22 April 2014
Program to count the votes of an election"""

print("Independent Electoral Commission")
print("--------------------------------")

votes=[]

vote=input("Enter the names of parties (terminated by DONE):\n") #input of all votes cast
print()

while vote!="DONE": #creates a list of all the votes cast
    votes.append(vote)
    vote=input("")
    
vote_dictionery={}

#creates a dictionery with each part and number of votes received
for vote in votes:
    if not vote in vote_dictionery:
        vote_dictionery[vote]=1
    else:
        vote_dictionery[vote]+=1

print("Vote counts:")
for vote in sorted(vote_dictionery): #can sort dictionery by using sorted
    final_count="{0:<10}".format(vote)
    print(final_count, "-", vote_dictionery[vote])
