
def vote():
    
    
    print('Independent Electoral Commission\n--------------------------------')
    #Input marks
    party_names=input("Enter the names of parties (terminated by DONE):\n")
    #Put names in list
    party_names_l=[]
    #Create Dictionaries
    party_final_votes={}
    while party_names !="DONE":
        #Put names in the list
        party_names_l.append(party_names)
        party_names=input("")
        if party_names=='DONE':
            break
        #Find the frequency of the party in the list if party is in the list 
        elif party_names in party_names_l:
            i=0
            party_name_votes=1
            while i <(len(party_names_l)):
                if party_names==party_names_l[i]:
                    party_name_votes+=1
                    party_final_votes[party_names]=party_name_votes
                
                
                i+=1
        #Declare the frequency of the party as one if party is not in the lists
        elif not party_names in party_names_l:
            party_name_votes=1
            party_final_votes[party_names]=party_name_votes 
    print()
    print('Vote counts:')
    #Print all the names of the party and the number of votes
    for party in (sorted(party_final_votes)):
        print(party,' '*(11-len(party)),'- ',party_final_votes[party],sep='')
    
              
                   
              
vote()