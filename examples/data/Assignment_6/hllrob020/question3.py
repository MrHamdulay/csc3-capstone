parties = [] #empty list for user inputs
Dict_parties = {} #dictionary to count frequenct of specific inputs

print('Independent Electoral Commission')
print('--------------------------------')
name = input('Enter the names of parties (terminated by DONE):\n')
while name != 'DONE' or name != 'done': #loop so that user can input list
    if name == 'DONE' or name == 'done': #boundary condition: no input
            break
    else:
        parties.append(name) #store entries in parties list
        name = input() 
        if name == 'DONE' or name == 'done': #ends loop if user types done
            break
if parties == []: #boundary condition print statement
    print()
    print('Vote counts:')
    print()
else:
    for party in parties: #to run through parties list
        if not party in Dict_parties: 
            Dict_parties[party] = 1 #records party in dictionary if it isn't there already
        else:
            Dict_parties[party] += 1 #adds one to element record in dictionary
    print()        
    print('Vote counts:')
    for party in Dict_parties: #runs through dictionary
        print('{0:<11}-{1:>2}'.format(party,Dict_parties[party]))
        