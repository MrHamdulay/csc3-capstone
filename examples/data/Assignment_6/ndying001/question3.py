'''Calculating votes of parties entered by user
 Inga Ndyoki
 25 April 2014'''

parties = []
votes = []
print('Independent Electoral Commission\n--------------------------------')
vote = input('Enter the names of parties (terminated by DONE):\n')
while vote != 'DONE':           #Allows user to enter party names until 'DONE' is entered
    votes.append(vote)
    if vote in parties:
        false = 1
    else:
        parties.append(vote)    #adds party name to party list
    vote = input()

frmat = '{name:<10}'
print()
print('Vote counts:')
parties.sort()
for i in range(len(parties)):
    print(frmat.format(name = parties[i]),'-',votes.count(parties[i])) #Prints out the party name with the number of votes accumulated