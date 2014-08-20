def votes():
    parties=[]
    parties_name=''
    maximum=10
    print('Independent Electoral Commission')
    print('--------------------------------')
    parties_names=input('Enter the names of parties (terminated by DONE):\n')   
    while parties_names != 'DONE':
        parties.append(parties_names)
        parties_names=input('')
        
    for i in range (len(parties)):
        if len(parties[i])> maximum :
            parties[i]=parties[i][0:12] #getting the maximum length
    print()
    print('Vote counts:')        
    for parties_names in sorted(set(parties)):
        print(parties_names,' '*(maximum-len(parties_names)+1),'- ',parties.count(parties_names),sep='') 
    
votes()