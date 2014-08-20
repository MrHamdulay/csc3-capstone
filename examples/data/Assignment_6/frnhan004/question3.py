"""Question 3-Assignment 6
FRNHAN004
24 April 2014"""


print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE): \n")
parties=[ ]
#ask user to enter a a party
party = input ()

while party != 'DONE':
    parties.append(party)
    party = input("")
    
counters={}
for word in parties: 
    if not word in counters: #if party not in list
        counters[word]=0 #add party to list
    counters[word] +=1 
print("Vote counts:")
for word in sorted(counters):
    print(word," "*(11-len(word)),"- ",counters[word],sep="")
    
    