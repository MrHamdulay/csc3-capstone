"""Assignment 6 Question 3
25 April 2014
Djavan Arrigone"""

def VotesCount():
    VoteCountDict = {}
    print("Independent Electoral Commission")
    print("--------------------------------")
    Votes = input("Enter the names of parties (terminated by DONE): \n")
    
    while Votes != "DONE":
        
        if Votes in VoteCountDict.keys(): #This if statement checks to see if the entry (vote) is already in the dictionary.
            VoteCountDict[Votes] += 1 #If the entry (vote) is found then it will add 1 too the corresponding key value. 
        else:
            VoteCountDict[Votes] = 1 #If the entry (vote) is not found in the dictionary, it will then create a new key for it.
        Votes = input("")
    print()
    print("Vote counts:")                   

    for key in sorted(list(VoteCountDict.keys())): #sorted function is used to sort the dictionary into alphabetical order. 
            print(key.ljust(10),"-",VoteCountDict[key]) #Right align the party names with width=10  


if __name__=='__main__':
    VotesCount()


