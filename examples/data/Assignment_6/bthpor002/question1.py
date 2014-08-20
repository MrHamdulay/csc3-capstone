#Program that prints out a right-aligned list
#Done by Portia Buthelezi 

def right_aligned():
    #create and empty string
    x_list= []
    #Let user enter the list
    x= input('Enter strings (end with DONE):\n')
    #append the inputs tp a list
    while x!= 'DONE':
        x_list.append(x)
        x= input('')
        
    #print the right aligned list
    print('\nRight-aligned list:')
    
    #find max length of the word in the list
    longest= 0
    for i in x_list:
        if len(i) > longest:
            longest= len(i)
        else: continue 
        
    for name in x_list:
        #print ou the spaces in order to allign the list
        spaces= longest - len(name)
        print(' '*spaces,name, sep='')
        
right_aligned() 