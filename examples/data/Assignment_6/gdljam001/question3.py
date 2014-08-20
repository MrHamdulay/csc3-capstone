"""Counting votes for parties
James Godlonton
24 April 2014"""

def voteSystem():#Main function for voting and tallying system
    print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")#Header
    name=""
    parties=[]
    while name!="DONE": #looping and adding input to array of all parties until stop sentinal is entered
        name=input("")
        if name!= "DONE":
            parties.append(name)
            
    dictOfPs={}
    for x in parties: #looping through array of parties adding unseen ones to dictionary and adding 1 to seen ones values (counting votes)
        if x in dictOfPs.keys():
            dictOfPs[x]=dictOfPs[x]+1
        else:
            dictOfPs[x]=1
            
    print("Vote counts:")
    keysAr=[]
    for var in dictOfPs.keys():#putting all keys into array for sorting
        keysAr.append(var)
    keysAr.sort()
    for part in keysAr:#goig through sorted array and printing the formated party name + number of votes
        print("{0:<10}".format(part)+" - "+str(dictOfPs[part]))
    
    
if __name__=="__main__":
    voteSystem()
        