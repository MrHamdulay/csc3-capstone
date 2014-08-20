#piet motalaota

def right_justified_list():
    
    
    names=[]

    name_request=input('Enter strings (end with DONE):\n')


    names.append(name_request)

    while 'done' not in names and "DONE" not in names:  

        name_request=input('')
        names.append(name_request)

    
    names.remove(names[-1]) 
    
    
    
    max=0
    for j in names:
        if len(j)>max:
            max=len(j)
    print('\nRight-aligned list:')

    for i in range(len(names)):
        print(names[i].rjust(max)) 
    

    
if __name__=='__main__':        
    right_justified_list()