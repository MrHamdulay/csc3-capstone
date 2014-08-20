"""voting counter
Lubalethu Dube
23 April 2014"""
def Mr_Votes():
    #print voting heading
    print("Independent Electoral Commission")
    print("--------------------------------")
    #get votes and put in list
    i=input("Enter the names of parties (terminated by DONE):\n")
    votes={}
    while i != "DONE" and i !=("done"):
        if i in votes:
            votes[i] += 1
        else:
            votes[i] = 1
        i=input("")
    #count votes
    print("\nVote counts:")
    for i in sorted(votes):
        print("{0:<10}".format(i), "-", votes[i])
Mr_Votes()  
        
        
        
        