#Thembekile Dubazana
#dbzphi002
#Assignment 6:Q3

"""Count the number of votes"""

#The input and variables
print("Independent Electoral Commission")
print("--------------------------------")
party=input("Enter the names of parties (terminated by DONE):\n")
partylist=[]
partydic={}

#The loop for list
while party!= "DONE":
    partylist.append(party)
    party=input() 
    for i in range(len(partylist)):#check number of occurences of party
        count=partylist.count(partylist[i])
        partydic[partylist[i]]=count

#Sorted list and formating
alph=sorted(partydic)
print()
print("Vote counts:")
for i in range(len(alph)):
    print('{0:10} - {1}'.format(alph[i],partydic[alph[i]]))
    
          
