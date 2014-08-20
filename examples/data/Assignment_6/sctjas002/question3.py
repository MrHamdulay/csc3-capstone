#25/04/2014
#Naadirah Ismail
#counts the number of votes per party and sorts them in alphabetical order

def count():
    print('Independent Electoral Commission')
    print('--------------------------------')
    name=input('Enter the names of parties (terminated by DONE):\n')#create dictionary and count the amount of times it occurs in the value    
    parties={}
    while name!='DONE':
        if name in parties.keys():#if it is in the dictionary add 1 count to value
            parties[name] =parties[name]+1
        else:
            parties[name]=1 #if its not in the dictionary add the key and a value of 1 
        name=input('')
    print('\nVote counts:')
    #format the names in a width of 10
    spaces=' '
    for name in sorted(parties):
        print(name,spaces*(10-len(name)-1),'-',parties[name])       
count()
