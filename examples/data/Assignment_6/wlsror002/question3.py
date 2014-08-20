def List():
    List=[]
    
    print('Independent Electoral Commission\n--------------------------------')
    
    x=input('Enter the names of parties (terminated by DONE):\n')
    while x != 'DONE' and x != 'Done' and x != 'done':
        List.append(x)
        x=input('')  
    
        
    return List

def dictionary(l):
    partys={}
    
    for i in l:
            partys[i]=partys.get(i,0)+1
    
    items=list(partys.items())
    items.sort()
    
    print('\nVote counts:')
    
    for i in range(len(items)):
        party,num_votes=items[i]
        print(party.ljust(10),'-',str(num_votes))
            

    
        
Votes=List()
dictionary(Votes)

