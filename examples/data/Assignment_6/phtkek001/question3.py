"""Kekolo Phetla
PHTKEK001
Assignment6 Question3"""

print("Independent Electoral Commission")
print("--------------------------------")
parties=[]
party_list=input("Enter the names of parties (terminated by DONE):\n")
while party_list != "DONE":
    parties.append(party_list)
    party_list=input("")
    
dicT={}
for i in parties:
    if not i in dicT:
        dicT[i]=1
    else:
        dicT[i]+=1

print('')
print("Vote counts:")        
for i in sorted(dicT.keys()):
    print(i.ljust(10),"-",dicT[i])
    
                   