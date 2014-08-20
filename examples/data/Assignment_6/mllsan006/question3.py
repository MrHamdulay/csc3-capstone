'''program to count the number of votes for each political party in an election
sankara mallane
22 april 2014'''

print('Independent Electoral Commission')
print('--------------------------------')

# get the names of parties from user
Party = []

xParty = input("Enter the names of parties (terminated by DONE):\n")
while xParty != 'DONE':
    Party.append (xParty)
    xParty = input("") 

# start with zero counters
counter = {}

# count xPartys and add new xPartys as they are encountered
for xParty in Party:
    if not xParty in counter:
        counter[xParty] = 1
    else:
        counter[xParty] += 1
print()        
print('Vote counts:')
 
number_of_space = 11                 
# print out vote counts
for xParty in (sorted(counter.keys())):

    print (xParty.ljust(number_of_space),'- ', counter[xParty],sep='')



    