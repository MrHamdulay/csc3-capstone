"""Assignment 6 , question 3
Yaseen Sulliman
20 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
parties=[] #create array
names=input("Enter the names of parties (terminated by DONE):\n") #input user for votes
parties.append(names)
while names!="DONE":
    names=input("")
    parties.append(names)

# create new array with each party only displayed once
limparties=[]
for x in parties:
    if x not in limparties:
        limparties.append(x)

print("")
print("Vote counts:")
parties.sort()
limparties.sort()

# print party and votes   
for j in range(1,len(limparties)):
    a=parties.count(limparties[j])
    print("{0:10}".format(limparties[j]),"-",a)

      
    
          



    
    