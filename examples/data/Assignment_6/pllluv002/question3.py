"""Vote counter
22/4/14
Luveshen Pillay"""

print("Independent Electoral Commission")
print("--------------------------------")
#Populate list
partylist=[]
a=""
while a != "DONE":
    if a == "":
        a=input("Enter the names of parties (terminated by DONE):\n")
        if a !="DONE":
            partylist.append(a)
    
    if a != "DONE":      
               a=input("")
               if a !="DONE":
                    partylist.append(a) 
               
#Process list to get number of parties               
partylist.sort()
try:
    
    

    c=partylist[0]
    numparty=[c]
    x=0
    for party in partylist:
        if party != c:
            numparty.append(party)
            
            c=party
            x+=1
except IndexError: 
    print("",end="")
print("\nVote counts:")
#Counting and printing
try:
    for party in numparty:
        count=partylist.count(party)
        print("{0:<10}".format(party)+" -",count)
        
except NameError: 
    print("")    
    



        