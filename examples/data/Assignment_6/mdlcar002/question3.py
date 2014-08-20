#assignment6 Question3
#Carissa Moodley
#program to count the number of votes in each political party in an election

def main():
    #For display purposes
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    parties=[]#declaring list called parties, this list will be used in the program
    countParties=[]#This list will count the votes for each party
    
    party=input()# this allows the user to enter a name of the party he/she wants to vote for
    while party!="DONE":#The user can keep entering names of parties until done is entered
        if(party in parties):# This checks to see if the party that the user currently entered has already been entered before. i.e second vote for that party
            countParties[parties.index(party)]+=1# if the party name has been entered before, this statement adds 1 to the countParties array at the same position that the party name is in in the parties array. so that if i say Parties[1], to get the number of votes i just have to say countParties[1]
        else:
            parties.append(party)# If the party hasnt been entered before. This adds the party name to the array parties to keeep track of all the parties that have been entered
            countParties.append(1)# This adds 1 vote to the party the first time it has been entered in the countParties array
        party=input()# This allows the user to enter another party name
    dicOfVotes={}# This declares a dictionary. This is for sorting purposes 
    for i in range(len(parties)):
        dicOfVotes[parties[i]]=countParties[i]# this assigns the party with the number of votes in the dictionary 
    print()#Leaves a line
    print("Vote counts:")
    for key in sorted(dicOfVotes):#this sorts the dictionary in terms of the Key. The key is the party name because no 2 parties can have the same name. So its easy to arrrange in alphabetical order
        print("{0:10} - ".format(key),end="")# Format statement to print the key
        print(dicOfVotes[key])#prints the number of votes associated with the key 
            
main()
            
        