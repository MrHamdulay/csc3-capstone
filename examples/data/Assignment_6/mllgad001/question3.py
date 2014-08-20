# program to count number of votes for each political party in an election
# mllgad001
# 22 April 2014


print("Independent Electoral Commission\n--------------------------------")

vote_list = [] # create empty list
vote = input("Enter the names of parties (terminated by DONE):\n") # prompt user to enter names of parties

while vote != 'DONE':
    vote_list.append(vote) # add votes to empty list
    vote = input("") # prompt user to enter more names until "DONE"

counters={} 

# calculate total number of votes of a party
for i in vote_list:
    if not i in counters:
        counters[i]=0
    counters[i] += 1
    
sort = sorted(counters.keys())

print("\n"+"Vote counts:")
for vote in sort:
    print(vote + ' '*(10 - len(vote)) ,'-',counters[vote])