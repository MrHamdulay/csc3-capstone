"""Sikhulile Thenjwayo
  Assignment 6
  23 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
parties = []
votes = []
#voting
vote = ""
print("Enter the names of parties (terminated by DONE):")
while True:
 vote = input("")
 if vote == "DONE":    
  break
 vote = vote + " "*(10 - len(vote))
 if not vote in parties:
  parties.append(vote)
  votes.append(1)
 else:
  count =0
  while True:
   if vote == parties[count]:
    votes[count] +=1
    break
   count+=1
  
#sort parties alphabetically
for k in range(len(parties)):
 parties[k] += "%"+ str(votes[k])
parties.sort()
for r in range(len(parties)):
 temp = parties[r].split("%")
 parties[r] = temp[0]
 votes[r] = eval(temp[1])

#display results

print("\nVote counts:")
for j in range(len(parties)):
 print(parties[j],votes[j],sep=" - ")
 
 