#danson masuka
#program to right align names input
#23 April 2014


def names():
    #make names into a list called names
    names = []
    nme = input("Enter strings (end with DONE):\n")
    while nme != 'DONE':
        names.append(nme)
        nme = input("")
    
    a = 0
    print()
    print ("Right-aligned list:")
    for i in names:
        if len(i) > a:
            a = len(i)
    for j in names:
        print (" "*(a-len(j))+j)
names()