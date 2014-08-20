"""The program on how to count votes for each political party
By Bruce Sontshot
20 April 2014 """

#introduction for voters
print("Independent Electoral Commission")
print("-"*32)

#creating the array for the names of parties
category = {}
partyNames = input("Enter the names of parties (terminated by DONE):\n")
while partyNames != 'DONE':
    category[partyNames]=category.get(partyNames,0)+1
    partyNames = input("")
#if the names of the parties are done    
if partyNames == 'DONE':
    x = list(category.keys())
    x.sort()
    print()     #space
    print("Vote counts:\n",end = "")
    counter = 0
    
    for i in range(len(x)):
        print((x[i]+((10-len(x[i]))*" ")),"-",category[x[i]])
       
    