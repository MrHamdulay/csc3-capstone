"""Program to count the number of votes in an election
Runako Muzwidzwa
23/04/2014"""
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
votes_str = []
#get votes in a string
while True: 
    votes=input()
    if votes=="DONE":
        break
    votes_str.append(votes)
    
#to make the vote string a list of seperated words
#sep_votes=votes_str.split(" ")
print()
print("Vote counts:")

#adding votes to dictionary
counter = {}
for vote in votes_str:
    if not vote in counter:
        counter[vote] = 1
    else:
        counter[vote] += 1

#sort the party votes
sorted_votes = sorted(counter.items(), key=lambda counter: counter[0])
for vote,counter in sorted_votes:
    space=(10-len(vote))
    print(vote," "*space+"-", counter)

    
    
    