def vote():
    print ("Independent Electoral Commission")
    print ("--------------------------------")
    Party_Names = []
    List_Names = []
    vote = input ("Enter the names of parties (terminated by DONE):\n")
    if vote == str("DONE"):
        jinx = 8
    else:
        Party_Names.append(vote)
        List_Names.append(vote)
    while vote != "DONE":
        vote = input ('')
        if vote not in Party_Names:
            List_Names.append(vote)
        Party_Names.append (vote)
        if vote == str("DONE"):
            del Party_Names[len(Party_Names)-1]
            del List_Names[len(List_Names)-1]
    
    #sorts party names 
    Hellion = sorted(List_Names)
    
    #counts votes
    print ()
    print ("Vote counts:")
    space = " "
    for i in Hellion:
        print (i,space*(10-len(i)-1),"-",Party_Names.count(i)) 
    
    
vote()