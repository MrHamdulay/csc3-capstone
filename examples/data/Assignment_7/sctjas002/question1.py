def _list():
    word=input('Enter strings (end with DONE):\n')
    _list=[]
    dicta={}  
    while word !='DONE':                    
            if word not in dicta: 
                    dicta[word]=1
                    _list.append(word)
            word=input('')
            
    print('\nUnique list:')
    for word in _list:
        print(word)
_list()
        
        
        
    
            