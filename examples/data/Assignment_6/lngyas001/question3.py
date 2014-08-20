"""program to count number of votes cast for specific parties
yasha longstaff 
23 april 2014"""

print('Independent Electoral Commission')
print('--------------------------------')

parties = input ('Enter the names of parties (terminated by DONE):\n')
party_list = []
if parties != "DONE":
    party_list.append(parties)

while parties != 'DONE':
    parties = input()
    if parties != 'DONE':
        party_list.append(parties)
    

single_list = []
for i in range(len(party_list)):
    if not party_list[i] in single_list:
        single_list.append(party_list[i])
    else:
        pass
single_list.sort()     
    
    
print('\nVote counts:')
for i in single_list:
    votes = party_list.count(i)
    print(i.ljust(10),'-',votes)
    

