'''duplicate elimination program
Ruchaan Schmidt
April 2014'''

def unique_list():                                          # primary list
    first = []                                              # start with empty list
    listgen = input('Enter strings (end with DONE):\n')     # generate list
    if listgen == 'DONE':
            print('\nUnique list:\n')                         # empty list
    else:
        while listgen != 'DONE':                            # create loop
            first.append (listgen)                          # add to list
            listgen = input ('')                            # empty string to type strings
    
        unlist = []                                         # empty unique list
        for i in first:                                     # iterate over first list
            if i not in unlist:
                unlist.append(i)                            # add first occurence to unique list
        print ('\nUnique list:')
        for j in unlist:
            print (j)

unique_list()