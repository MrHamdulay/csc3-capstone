# program to count the number of votes for each political party in an election
# khadeejah omar
# 21 april 2014

heading = "Independent Electoral Commission"
print(heading + "\n" + ("-" * len(heading)))

vote = input("Enter the names of parties (terminated by DONE): \n")
vote_list = []
if vote != "DONE" :
    vote_list.append(vote) # store first vote

while vote != "DONE" : 
    vote = input("")
    if vote != "DONE" :
        vote_list.append(vote)  # store each vote after the first vote

vote_counter = {}
# store the number of each vote
for vote in vote_list :
    if vote not in vote_counter :
        vote_counter[vote]  = 0
    vote_counter[vote] += 1

sorted_votes = sorted(vote_counter.keys())

print("\n" + "Vote counts: ")

for vote in sorted_votes :
    print(vote + " "*(10 - len(vote)) + " -", vote_counter[vote])