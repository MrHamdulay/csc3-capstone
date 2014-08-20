# Lehlogonolo Masetla
# 20 April 2014

print('Independent Electoral Commission')
print('--------------------------------')

votes = [] # introduces the array with no items

# asks the user for the first candidate
names = input('Enter the names of parties (terminated by DONE):\n')

#width = len(names) 

# continues asking for name until the user prints DONE
while names != 'DONE':
    votes.append(names)
    names = input('')
    
    # Keeps the length of the longest item
#    if len(names)>width:
#        width = len(names)
        
votes.sort() # sorts the list is alphabetical order

temporary_list = [] # introduces a temporary empty loop

print("")
print('Vote counts:')

for i in range(len(votes)):
    
    # loop that stores the printed item into the temporary list and avoid printing more than once
    if votes[i] not in temporary_list:
        print(votes[i]," "*(11-len(votes[i])),"-"," ",votes.count(votes[i]),sep="")
        temporary_list.append(votes[i])