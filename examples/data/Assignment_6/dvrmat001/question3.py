"""counts number of votes for a number of politcal parties
23 april 2014
yuan-yow wu"""

print("Independent Electoral Commission")
print("--------------------------------")
parties = []
print("Enter the names of parties (terminated by DONE):")
votes = ""
while votes.lower() != "done":
    votes = input()
    if votes.lower != "done":
        parties.append(votes)
del parties[len(parties)-1]


print("\nVote counts:")

count = 0
for i in range (len(parties)):
     
        if i == 0:
            number = 1
            count = i + 1
        elif sorted(parties)[i-1] != sorted(parties)[i]:
            number = 1
            count = i + 1
        else: 
            continue
                
        while count < len(parties):
            
            if sorted(parties)[count-1] != sorted(parties)[count]:
                break            
            elif sorted(parties)[count-1] == sorted(parties)[count]:
                number += 1
                count +=1
        print(sorted(parties)[i]," "*(9-len(sorted(parties)[i])),"-",number)
                


        
