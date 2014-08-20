"""Program to simulate voting at the ballots
Sabelo Xulu
22 April 2013"""

print("Independent Electoral Commission")
print("--------------------------------")

#empty lists to collect the candidate names 
candidates=[]
word=[]
newcandidates={}
x=0
partynames=input("Enter the names of parties (terminated by DONE):\n")
if partynames=="DONE":
        while x:
                break
        
        

else:
        candidates.append(partynames)
#loop that allows indefinite input of values
while partynames != "DONE":
        partynames=input("")
        if partynames!= "DONE":
                candidates.append(partynames)
print()
print("Vote counts:")
candidates.sort()
# loop that counts number of votes
for i in range(len(candidates)):
        #this check examines whether the word in list:candidates has already been counted.
        #If so, it is skipped, as it is already counted
        if candidates[i] in word:
                continue        
        else:
                x=candidates.count(candidates[i])
                word.append(candidates[i])
                print("{0:<10}". format(candidates[i]),"-",x)
               
                
        
        
                

                