'''right aligns a list of strings entered by the user
tom new
2014/04/12'''

def getlist ():
    '''Gets a list of strings from the user'''
    # creates list of strings
    strings = []
    
    # gets strings from user
    while True:
        #checks if current input is the first string entered
        if strings == []:
            string = input ()
            if string == 'DONE':
                return strings
            strings.append (string)        
        else:
            string = input ()
            if string == 'DONE':
                return strings
            strings.append (string)
        
def maxlength (array):
    '''Finds the longest string in a list'''
    maxl = 0
    for i in array:
        # checks if current item is longer than current max length
        if len (i) > maxl:
            maxl = len (i)
    return maxl

def alignr (array):
    '''Prints a list in right-hand alignment'''
    maxl = maxlength (array)
    for i in array:
        print (' ' * (maxl - len (i)), i, sep = '')
        
if __name__ == '__main__':
    print ('Enter strings (end with DONE):')
    array = getlist ()
    print ()
    print ('Right-aligned list:')
    alignr (array)