'''Right-alignement Program
Sbongakonke Mlangeni
20 April 2014'''



def xy():
    #Taking strings
    strinng = input('Enter strings (end with DONE):\n')
    strinngs = []
    lengths = []
    while strinng != 'DONE':
        #creating a list of strings
        strinngs.append(strinng)
        strinng = input('')
    
    for i in strinngs:
        #creating a list of lengths
        lengths.append(len(i))
    #a = max(lengths)
    print('')
    print('Right-aligned list:')
    for i in strinngs:
        #Printing in right-aligned
    
        #space = a - len(i)
        print(' '*(max(lengths) - len(i))+i)
        
    
    
xy()