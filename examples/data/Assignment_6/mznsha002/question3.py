# 24 April 2014
# Shaun Muzenda
# Counting the number of votes an undetermined number of parties receive in an election

def main():
    print("Independent Electoral Commission")
    print("-" * 32)
    

    party_names = []      #empty string with party party_names
    party_name = input ("Enter the names of parties (terminated by DONE):\n")  #inputing party names
    party_name_list = party_name.split(" ")

    while party_name != "DONE":             #inputing DONE stops the counting of votes
        party_names.append (party_name)     #adding the inputed data to the party_names string
        party_name = input ("")

    print()
    
    print("Vote counts:")  
    votes_counter = {}           #creating a dictionary to start count of votes
    
    for party_name in party_names:      #looping through the list for inputed name       
        if party_name not in votes_counter:
            votes_counter[party_name] = 1   #starts count of a new party name
        else:
            votes_counter[party_name] += 1      #adds votes to each parties dictionary
    
    for party_name in sorted(votes_counter):       #sorts the different party names in alphabetical order
        print ("{0:<10}".format(party_name),"-",votes_counter[party_name])    #formats the party names in a field with width=10 to create the effect of columns
        
main()
    