'''a module that removes duplicate items from a list
tom new
2014/04/28'''

def getlist ( ):
    '''Gets a list of strings from the user'''
    # creates list of strings
    strings = [ ]
    
    # gets strings from user
    while True:
        
        #checks if current input is the first string entered
        if strings == [ ]:
            string = input ( )
            if string == 'DONE':
                return strings
            strings.append (string)        
        else:
            string = input ( )
            if string == 'DONE':
                return strings
            strings.append (string)
            
def remove (array):
    '''Removes duplicate items from a list'''
    checker = { }
    indexer = [ ]
    
    # creates a list containing the indexes of occurences of duplicate items in array
    for i in range (len (array)):
        if array [i] in checker:
            indexer.append (i)
        else:
            checker [array [i]] = 'present'

    # reverses the list of indexes so the next step works backwards
    indexer.reverse ( )

    # removes the duplicate items
    for i in indexer:
        del array [i]
        
if __name__ == '__main__':
    print ('Enter strings (end with DONE):')
    array = getlist ( )
    print ( )
    print ('Unique list:')
    remove (array)
    for i in range (len (array)):
        print (array [i])