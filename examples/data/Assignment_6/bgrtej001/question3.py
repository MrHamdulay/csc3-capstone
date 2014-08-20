"""Question 3, Assignment 6
Tejasvin Bagirathi BGRTEJ001"""


print('Independent Electoral Commission')
print('-'*32)
print('Enter the names of parties (terminated by DONE):')

#Declare empty string
string = ""
votes = []

#User inputs votes until done
while string != 'DONE':
    votes.append(string)
    string = input('')
    
    
print()
print('Vote counts: ')
#Declare new list
parties = []
#Loop to determine parties involved
for i in votes:
    if i in parties or i == 'DONE' or i == '':
        continue
    else:
        parties.append(i)
        
parties=sorted(parties)

#Nested loop to count votes for each party
for j in parties:
    counter = 0
    for h in votes:
        if j == h:
            counter += 1
        else: continue
        spaces = 10-len(h)
    print(j, spaces*' ', ' - ', counter, sep='')
    
    
