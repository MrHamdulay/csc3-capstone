'''program to enter parties and return the votes per party
Norman Pilusa
April 2014'''
 
def vote():
    print('Independent Electoral Commission')
    print('-'*len('Independent Electoral Commission'))
    parties=[]#list of parties
    new=[] #parties without repetition
    
    party=input('Enter the names of parties (terminated by DONE):\n')
    while True: #add parties to list
        if party=='DONE':
            break
        else: 
            parties.append(party)
            party=input()
    print()
    print('Vote counts:')
    parties.sort()
    for party in parties:
        if party not in new:
            new.append(party)
            count=parties.count(party)
            print(party.ljust(11)+'-',count)#right alignment of vote counts
        else: continue
   
        
vote()