#types of votes
#create empty votelist
votelist=[]
votetally={}
#introduction
print("Independent Electoral Commission")
print("--------------------------------")

#prompt for votes
vote=input("Enter the names of parties (terminated by DONE):\n")

#prompt for more votes
while vote!="DONE":
    votelist.append(vote)
    vote=input("")

for vote in votelist:
    if not vote in votetally:
        votetally[vote]=0
    
    votetally[vote]+=1

sorted_parties = sorted(votetally.keys())
        
print("\n""Vote counts:")
for vote in sorted_parties:
    print(vote + ' '*(10 - len(vote)) ,'-',votetally[vote])
