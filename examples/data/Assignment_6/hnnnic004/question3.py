'''program for counting votes
nicole henning
due: 25 april 2014'''

#print title
#ask for list
#stop when done
#show vote counts

#print opening title
print("Independent Electoral Commission")
print("--------------------------------")

#make empty list
votes_tot = []

#get votes
votes_str = input("Enter the names of parties (terminated by DONE):\n")
while votes_str != "DONE":
    votes_tot.append(votes_str) #add each vote to existing list
    votes_str = input("")  

votes_tot.sort() #sort into alphabetical order

print()

#find no of repetitions of votes for parties
def find_rep (a):
    count = votes_tot.count(a)
    return count        
    
print("Vote counts:")

rep = []
#print no of votes foe each party
for i in votes_tot:
    if i not in rep: #restricts printing party and number of votes to once, ie not reps
        rep.append(i)
        print("{0:<11}".format(i),"- ", find_rep(i) ,sep="")
        