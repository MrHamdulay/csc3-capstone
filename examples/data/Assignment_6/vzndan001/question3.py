"""tallying votes for a given party
danica van der zandt
24 march 2014"""



#heading of the program seen by user
welcome=("Independent Electoral Commission")
length_welcome=len(welcome)
print(welcome)
print("-"*length_welcome)


#getting input values from the user
votes=[]
party=input("Enter the names of parties (terminated by DONE):\n")
while party != "DONE":
    votes.append(party)
    party=input("")
    

    
           
        
#create a dictionary where the party names are the keys and the number of votes the value
#the keys will stay the same but the party votes will change
tally={}
for j in votes:
    tally[j]=tally.get(j,0)+1
#print(tally)
sorted_tally=sorted(tally)
#print(sorted_tally)
#print it side by side
print("\nVote counts:")


for key in sorted_tally:
    print(key.ljust(10),"-",tally[key])
    

    