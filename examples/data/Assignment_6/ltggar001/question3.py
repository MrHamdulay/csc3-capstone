'''program to count duplicates of words and then display th results
Gareth Lategan
25-04-2014'''
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")

votes = []

def vote():
    a=input()
    if a != "DONE":
        votes.append(a)
        vote()
vote()
votes.sort()
print("\nVote counts:")

v=0
for i in range(len(votes)):
    if v<len(votes):
            a=votes.count(votes[v])
            print(votes[v]," "*(11-len(votes[v])),"- ",a,sep="")
            v+=a