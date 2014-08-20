"""program to count votes
Author: Rofhiwa Liphauphau
Date: 25 April 2014"""
print("Independent Electoral Commission")
print("--------------------------------")


names=input("Enter the names of parties (terminated by DONE):\n")
parties=[] #empty list
while names!="DONE":
     parties.append(names)# putting all inputs into list
     names=input("") 

parties.sort() #putting inputs into alphabetical order
counter={} #Creating a dictionary
print()
print("Vote counts:")
for i in parties:
     if not i in counter: #inserting corresponding count to the dictionary
          counter[i]=parties.count(i)
          print(i," "*(9-len(i)),"-",counter[i])


