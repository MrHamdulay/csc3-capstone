"""Program that prints names aligned
Aubrey Baloi
22 April 2014"""

def names():
    names = [] # Get an input of names 
    name = input('Enter strings (end with DONE):\n')
    
    if name == 'DONE':
        print('\nRight-aligned list:')
    else:
    
        while name != 'DONE':
            names.append(name)
            name=input()
        
        print('\nRight-aligned list:')
        long_name =max(names, key=len) #find maximum value in terms of length
        long_length = len(long_name)
    
    for i in names:
        print(" "*(long_length-len(i)),i, sep='')
    

names()