def namelist():
    #This first set of instructions formulates the list to be aligned 
    y = []
    x = input ("Enter strings (end with DONE):\n")
    if x == str("DONE"):
        s=2
    else:
        y.append(x)
    while x != "DONE":
        x = input ('')
        y.append (x)
        if x == str("DONE"):
            del y[len(y)-1]
    
    # This list assesses the length of all the names in the list
    b=[]
    for a in y:
        c = len(a)
        b.append(c)
        c=0
   
    # This part finds the largest name in the list
    start = 0
    for listnum in b:
        if listnum > start:
            start = int(listnum)
    
    # This prints the list right-aligned
    space = 0
    print ("")
    print ("Right-aligned list:")
    for word in y:
        space = start - len(word)
        print (" "*space, word,sep="")
        
namelist()