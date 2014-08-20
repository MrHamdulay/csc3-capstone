#parties
#B.Booi
#24 April 2014
import pprint

def countParties():
    listOfP=[]
    i = 0
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    while i != -1:
        vote = input("")
        if vote == "DONE":
            i = -1
        else:
            i+1 
            listOfP.append (vote)
            
    
    Votecounter={}
    for vote in listOfP:
        if vote in Votecounter:
            Votecounter[vote] +=1
        else:
            Votecounter[vote] = 1    
    print()
    print("Vote counts:")
    
    #keys = D.keys()
    #values = D.values()
    #D.sort()
    for vote in sorted(Votecounter.keys()):
        print("{0:<10}".format(vote)," - ",Votecounter[vote],sep="")

countParties()
    
    
        
    