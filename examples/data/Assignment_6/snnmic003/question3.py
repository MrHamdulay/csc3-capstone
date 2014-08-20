'''Votes in an election
Michael Sanne
2014/04/20'''

#Prints Opening Lines
print ("Independent Electoral Commission")
print ("--------------------------------")

#Asks the user for input on the votes and stores them as a list
party_str = input("Enter the names of parties (terminated by DONE):\n")
party = [party_str]
while party_str != "DONE":
    party_str = input ("")
    party.append(party_str)
    
#Creates and Stores a list with the names of the parties and a 2nd list for the final output

parties = []
final = []
#length of list minus done
for i in range (len(party) - 1):

    key = party[i]
    if (key in parties):
        continue      
    else: 
        parties.append(key)
        final.append ('{0:<10}'.format(str(key)) + " - " +str(party.count(key)))
        
final.sort()
print ()
print ("Vote counts:")
for j in range (len(final)):
    print (final[j])