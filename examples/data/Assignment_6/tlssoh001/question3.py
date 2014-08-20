#program to tally votes
#Sohail Tulsi TLSSOH001
#23 April 2014

print('Independent Electoral Commission')
print('--------------------------------')

#add votes to list
votes= []
vote= input('Enter the names of parties (terminated by DONE):\n')
while vote != 'DONE':
    votes.append(vote)
    vote= input('')

#sort list
votes.sort()

#count votes per person
count = 1
print('')
print('Vote counts:')
for i in range(1,len(votes)):
    
    if votes[i-1] == votes[i]:
        count += 1
        
    else:
        print(votes[i-1],' '*(9-len(votes[i-1])),'-', count)
        count=1
        
# count for last set of votes
for i in range(1,len(votes)):
        
    if i==len(votes)-1:
        print(votes[i],' '*(9-len(votes[i])),'-', count)    
        
    