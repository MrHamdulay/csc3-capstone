'''right-align relative to longest string in list program
Ruchaan Schmidt
April 2014'''

def rightalign():
    string = []                                         # start with empty lists
    listgen = input('Enter strings (end with DONE):\n') #generate list
    while listgen != 'DONE':                            #create loop
        string.append (listgen)                         #add to list
        listgen = input ('')                            #empty string to type strings
    width = max(string,key=len)                         #find max in list
    print ('\nRight-aligned list:')
    strlen = len(width)    
    for i in string:                                    #calculate length of strings in list
        print (i.rjust(strlen))    
rightalign()