"""program #keeto output parties with their vote counts
yondela nkwali
20 April 2014"""

#printout the title
print("Independent Electoral Commission")
print("--------------------------------")
Lparties=[]
Lparties2=[]
Pname=input("Enter the names of parties (terminated by DONE):\n")
#get list of party names(acount for "DONE")
if Pname=="DONE":
    print("\nVote counts:\n")
else:
    while Pname!="DONE": 
        Lparties.append(Pname)
        Pname=input("")
        Lparties.sort()
    #keep track of no of times a party appears and remove duplicates      
    print("\nVote counts:")
    for names in Lparties:
        nVotes=Lparties.count(names)
        if names in Lparties2:
            continue
        """to print out names with vote counts
        assume all names are of lengh 10 wide"""     
        Lparties2.append(names)
        print("{:10} {} {}".format(names,"-",nVotes,sep=""))  
