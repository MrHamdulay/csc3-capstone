#prog for counting up votes of parties 

print('Independent Electoral Commission')
print('--------------------------------')


def parties():
    #create an empty dictionary
    party_list = {}
    #get party inputs
    party = input('Enter the names of parties (terminated by DONE):\n')
    #if user does not input DONE then add input to the dictionary 
    print()
    while party!='DONE':
        #if the input already exists in the dictionay then add 1 to its value 
        if party in party_list:
            party_list[party]+=1
        #otherwise add the new input to the dictionary with a value of 1     
        else:
            party_list[party]=1
        party = input('')
    #loop through the items in the dictionary, have the number of spaces between the party name and votes set to 11, and the for every key subtract its length from 11 and the print the key then the difference of the key and then the value of votes 
    
    print('Vote counts:')
    
    for key, value in sorted(party_list.items()):
        space = 11-len(key)
        print( key + space*' ' +'- '+ str(value))    
        
parties()
