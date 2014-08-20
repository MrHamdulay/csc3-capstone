'''Write a program to count the number of votes for each political party in an election.
Sinead Urisohn
19 April 2014'''

print("Independent Electoral Commission\n--------------------------------")
#Get input
name=input("Enter the names of parties (terminated by DONE):\n")
#set vote counter as array
vote=[]
#set empty part name array
party=[]


#create output variable
out=""
#loop until sentinel entered
while name!="DONE":
    #append every name entered to vote
    vote.append(name)
    #append unique names to party
    if name not in party:
        party.append(name)
    
    #ask for input again
    name=input()

#initialise vote per party variable
reference={}
for i in range(len(party)):
    #set key as party and number of votes as values that key refers to
    reference[party[i]]=vote.count(party[i])
#sort names of parties alphabetically
party=sorted(party)
# Format party names in a field with width=10 to create the effect of columns 
txt="{0:<10}"
#print data
print("\nVote counts:")
for i in range(len(party)):
    counteach=reference[party[i]]
    print(txt.format(party[i]),"-",counteach)


