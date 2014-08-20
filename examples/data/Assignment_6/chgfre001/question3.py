#vote counting program
#F.J.Chigwaza
#24-04-2014

def vote_counter():
    print('Independent Electoral Commission\n--------------------------------')
    
    name=input('Enter the names of parties (terminated by DONE):\n')
    party=[]
    while name!='DONE':
        party.append(name)
        name=input('')
        
        
       
    counter ={}
        
    for name in party:
        if name not in counter:
                counter[name]=1
        else:
                counter[name]+=1
    print("\nVote counts:")       
    for item in sorted(counter.keys()):
       
        #print(item,counter[item])
        a=11-len(item)
        strin=str(counter[item])
        
        print(item+" "*a+"-"+' '+strin)     
        
vote_counter()        
        
        
        
    
    
