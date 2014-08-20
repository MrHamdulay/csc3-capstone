"""Cherise Dube
20 April 2014
Program to count a number of votes"""

print("Independent Electoral Commission")
print("--------------------------------")
partynames=input("Enter the names of parties (terminated by DONE):\n")
party_list=[]

while partynames !='DONE':
    party_list.append(partynames)
    partynames=input("")

#Counts the votes and creates partyname:count pair in dictionary
vote_dictionary={}
for i in party_list:
    if i in vote_dictionary:
        continue
    else:
        count=party_list.count(i)
        vote_dictionary[i]=count
        
#Sorts the vote dictionary by keys then prints the partyname=key and number of corresponding votes=values 
print()
print("Vote counts:")
for i in sorted(vote_dictionary):
    space=9-len(i)
    print(i," "*space,"-",vote_dictionary[i])
    
    
    
    
        

    
    