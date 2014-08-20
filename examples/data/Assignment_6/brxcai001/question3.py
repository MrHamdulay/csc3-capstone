#Programe to count number of votes for specific parties.
#BRXCAI001
#25 April 2014

#Create an empty list.
parties = []

#Get a list of party names that stops getting names when DONE is entered.    
print("Independent Electoral Commission")
print("--------------------------------")
partyname = input("Enter the names of parties (terminated by DONE):\n")

while partyname != "DONE":
    parties.append(partyname)
    partyname = input("")

#Check the amount of occurences of a party name in the list of party names.  
print("\nVote counts:")
parties.sort()
counted = ''
for partyname in parties:
    if partyname not in counted:
        
        x = parties.count(partyname)
        form = "{0:<10}".format(partyname)
        print(form,"-",x)
        counted += partyname
    
    
    
    
    
    
    
    
    
    



