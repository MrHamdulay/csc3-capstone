#Shaaheen Sacoor SCRSHA001
#19 April 2014
#Program to enter electorial party votes into a list and count the votes for each party

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    parties = input("Enter the names of parties (terminated by DONE):\n")
    votes =[] #Empty list
    while parties !="DONE":
        votes.append(parties) #Adding parties to list
        parties = input("")
    print("\nVote counts:")
    votes.sort() #Sorting list
    repeats= [] #List for all repeated parties
    formatvote = '{0:<11}'
    for i in range(len(votes)): #Goes through party list(votes)
        if votes[i] in repeats:
            print("",end="") #If party has already been accounted for then print nothing
        else:
            print(formatvote.format(votes[i]),"- ",votes.count(votes[i]),sep="") # else print the vote count
        repeats.append(votes[i]) #Adds to repeat list so it won't be used again
main()
    
    
        