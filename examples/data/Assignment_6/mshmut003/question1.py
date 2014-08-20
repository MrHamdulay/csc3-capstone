# Right justifeir
# Mutali Mahshamba
# 14 April 2014

def justifier ():
    # Get strings from user
    strings = input("Enter strings (end with DONE):\n")
    # Create an empty list in which strings will be stored
    nameList = []
    # Add strings to the list
    while strings != 'DONE':
        nameList.append(strings)
        strings = input('')
    maxima = 0
    # Get the lenght of the longest string in the list
    for i in nameList:
        lt = len(i)
        if lt > maxima:
            maxima = lt
    print('\nRight-aligned list:')
    for i in nameList:
        print(' '*(maxima-len(i))+i)
    # Be Happy
justifier()
    