#Naadirah Ismail
#25/4/2014
#sorts out an input list of names into a list and 


def names():
    names=input('Enter strings (end with DONE):\n')
    _list=[]#converts input to list
    
    while names !='DONE':#asks for input and adds it to the list
        _list.append(names)
        names=input('')
    mx=0  #finds the max length to format it into a right aligned list
    for i in _list:
        if len(i)>mx:
            mx=len(i)
    print('\nRight-aligned list:')        
    for i in _list:
        spaces=mx-len(i)
        print(' '*spaces+i,sep='')
names()        
               
        

         

        
    
        
                
    
            
            
        
    