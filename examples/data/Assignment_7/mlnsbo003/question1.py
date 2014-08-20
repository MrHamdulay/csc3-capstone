'''Prints the entered list in the same order excluding repeated characters
Sbongakonke Mlangeni
28 April 2014'''

def xy():
    listnames = []
    names = input('Enter strings (end with DONE):\n')
    while names != 'DONE':
        if names in listnames:
            names = input()
        else:
            listnames.append(names)
            names = input()
    print('')
    print('Unique list:')
    for i in listnames:
        print (i)
            
xy()
            