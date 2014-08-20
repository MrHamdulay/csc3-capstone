""" Bella Gorham
voting
20/04/2014"""

# empty lists
parties = []
finalparties= []
answerlist= []
vote=""

# ask for input until done
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
while vote != "DONE":
    vote=input()
    parties.append(vote)
    parties.sort()
parties.remove("DONE")




pair=[]



for i in parties:
    #make count parties
    answer = parties.count(i)
    if [i,answer] in answerlist:
        # elimainate dulpicates
            continue
    #new list of parties and votes
    pair = [i, answer]
    answerlist.append(pair)
    

        

print()
print("Vote counts:")
final = "{0:<10} - {1}"
for p in answerlist:
    #spliting list
    partyname = p[0]
    votes = p[1]
    #format for display
    print(final.format(partyname,votes))













