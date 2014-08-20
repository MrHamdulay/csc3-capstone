#Program to count votes
#Nevarr Pillay - PLLNEV006
#22 April 2014

votes = {}
listofparties = []

def votesIn(): #Inputs all the votes until the sentinel is reached
    vote = input("Enter the names of parties (terminated by DONE):\n")
    while vote != "DONE":
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
        vote = input()
    print()    

def outputVotes(): #Prints out all the votes in alphabetical order   
    for key in votes:
        listofparties.append([key,votes[key]]) #Adds the party and its number of votes to a 2D array
    listofparties.sort() #Array is sorted alphabetically by the parties
    print("Vote counts:")
    voteout = "{0:<10} - {1}"
    for i in listofparties: #Outputs all the parties according to the format
        party = i[0]
        numVotes = i[1]
        print(voteout.format(party,numVotes))    

def main():
    heading = "Independent Electoral Commission"
    print(heading)
    print("-"*len(heading))
    votesIn()
    outputVotes()
    
if __name__ == "__main__":
    main()