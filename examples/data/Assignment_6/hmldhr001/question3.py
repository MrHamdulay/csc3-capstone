
#Dhriven Hamlall
def main():
    
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    theListOfParties=[]
    count=[]
    
    party=input("Enter the names of parties (terminated by DONE):\n")
    
    while party!="DONE":
        if(party in theListOfParties): #checks the list for repetiton of party
            count[theListOfParties.index(party)]+=1 #counting 
        else:
            theListOfParties.append(party)
            count.append(1) # as this is the first time the new party is entered and obviously its the first count
        party=input()
        
    Votes={}
    
    length=len(theListOfParties)
    for i in range(length):
        Votes[theListOfParties[i]]=count[i]
    print()
    
    print("Vote counts:")
    for j in sorted(Votes):
        print("{0:10} - ".format(j),end="")
        print(Votes[j])
            
main()