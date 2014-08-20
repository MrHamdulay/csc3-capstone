print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
Parties = {}
enter = ' '
#Parties={'apples': 1, 'oranges':1, 'p':pears}
while enter!='DONE':
    enter=input()
    if enter!='DONE':
        
        if enter in Parties:
            Parties[enter]+=1
          
        else:
            Parties[enter]=1

#total votes now calculated
print()
print('Vote counts:')



for party,votes in sorted(Parties.items()):
    print(format(party,'10s')+' - '+str(votes))
    
    