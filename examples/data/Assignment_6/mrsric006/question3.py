def q3():
    print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")    
    a = []
    j=0
    b= []
    while j != 'DONE':           #keep inputting til 'DONE'
        j = input('')
        if j != 'DONE':          #List A collects everything that is inputted
            a.append(j)       
        if j not in b and j != 'DONE':    #list b collects every unique input (like each diff party)
            b.append(j)
        b.sort()                       #sorts list alphabetically magically
    print()
    print("Vote counts:")
    for i in b:                     #for every unique party in list b count the number of those that appear in list a
        y = a.count(i)
        g = str(y)        
        f = "{0:<11}"        
        print(f.format(i),'- ',g,sep='')        #formatted printing 
        
q3()

