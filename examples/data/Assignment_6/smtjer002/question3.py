"""a program to count the number of votes for a list of political parties
by Jeremy Smith SMTJER002
21 April 2014"""

#input a list of votes
vote_list = []
print("Independent Electoral Commission\n--------------------------------")
vote = input("Enter the names of parties (terminated by DONE):\n")
vote_list.append(vote)
while vote != "DONE":
    vote=input()
    vote_list.append(vote)

del vote_list[-1]

#create a list of the parties and sort them in alphabetical order
party_list = []
for party in vote_list:
    if party not in party_list:
        party_list.append(party)
        
party_list.sort()

#a function to count the votes
def count_votes(votes):
    vote_count = vote_list.count(votes)
    return vote_count

#output the party with the number of votes
print("\nVote counts:")
for i in party_list:
    count = count_votes(i)
    party_align = "{0:<10}"
    print(party_align.format(i)," - ", count, sep="")