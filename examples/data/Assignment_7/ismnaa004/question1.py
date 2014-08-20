#naadirah ismail
#3/4/14
#prints out list of words entered with no duplications, in same order


def _list():
    word=input('Enter strings (end with DONE):\n')
    _list=[]
    dicta={}   #create list and dict. 
    while word !='DONE':                    
            if word not in dicta: #add word to dict if its not in
                    dicta[word]=1
                    _list.append(word)#then append it to the list so its easy to print and maintains the original order
            word=input('')
            
    print('\nUnique list:')
    for word in _list:
        print(word)
_list()
        
        
        
    
            