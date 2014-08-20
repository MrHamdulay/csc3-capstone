"""Program for voting
Geoff Murphy
MRPGEO001
20 April 2014"""

parties = []
votes = []

print("Independent Electoral Commission")
print("--------------------------------")
vote = input("Enter the names of parties (terminated by DONE):\n")

#-------------------------------------------------------------------------------
    
while vote != "DONE":
    if vote in parties:
        pass                #Tells the loop to do nothing
    else:
        parties.append(vote)    #If it is a new party, it adds it to the list of parties

    if vote == "DONE":      #Ends the while loop if sentinel value, 'DONE', is entered       
        break
    votes.append(vote)
    vote = input("")

#-------------------------------------------------------------------------------
print("")

parties_dic = {}
for i in parties:    #Turns the given list into a dictionary
    parties_dic[i] = 0
    
for i in parties_dic:       #Then tallies the total votes for each party
    for j in votes:         
        if i == j:          #Checks if the party name corresponds with the vote
            parties_dic[i] +=1 #If so, it adds one point to the respective party's tally


#-------------------------------------------------------------------------------

print("Vote counts:")           
for i in sorted(parties_dic):  #Sorts the parties alphabetically
    print('{: <10}'.format(i), '-', parties_dic[i]) #Prints the results with a minimum column width of 10, excluding word characters, and prints the total votes.
    

        
    

