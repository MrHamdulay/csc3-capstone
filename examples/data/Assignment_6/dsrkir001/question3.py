#Program to count the number of votes for each political party in an election
#20 April 2014
#Kiran Desraj


print("Independent Electoral Commission")
print("--------------------------------")

#Get list

parties = []
party = input('Enter the names of parties (terminated by DONE):\n')


while party != 'DONE':       #use 'DONE' as sentinel
    parties.append(party)
    party = input('')

print('')

parties2 = []               #Empty list

parties.sort()           #Puts list in alphabetical order

print('Vote counts:')
for party in parties:
    if not party in parties2:    #Check if item is in parties2
        parties2.append(party)    #moves item to parties2
        print('{0:<10}'.format(party),' ','-',' ',(parties.count(party)), sep='')

