#Election Results
#4/22/2014
#Sydney Simpson

#Score
def score(votes):
    results={}
    for item in votes:
        if item not in results:
            results[item]=0
        results[item]+=1
    return results
#Get votes
print("Independent Electoral Commission")
print("--------------------------------")
votes=[]
choice=0
print("Enter the names of parties (terminated by DONE):\n")
while choice!="DONE":
    choice=input()
    if choice!="DONE":
        votes.append(choice)
    
results=score(votes)

print("Vote counts:")
#sorted(results) 
for i in sorted(results):
    c=10-len(i)
    d="{0:10} -"
    print(d.format(i),results[i])
    
    