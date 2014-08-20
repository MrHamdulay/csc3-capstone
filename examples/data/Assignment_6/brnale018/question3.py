# Program to count the number of votes in an election
    
print("Independent Electoral Commission")
print("--------------------------------")
party_names = input("Enter the names of parties (terminated by DONE):\n") #get names
parties_list=[] #create empty list
while party_names != "DONE":
        parties_list.append(party_names) #add input to list    
        party_names=input('')
            
each_party=[]
for j in parties_list: 
        if j in each_party:
                continue #if string in list, continue loop
        else:
                each_party.append(j) #add strings
                
each_party.sort()
print("\nVote counts:")

for i in range (len(each_party)):
        print(each_party[i] , (9 - len(each_party[i]))*" " , "-" , parties_list.count(each_party[i])) #format list


                
        
    
    
