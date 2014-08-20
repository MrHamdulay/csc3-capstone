#Kieran Reilly, RLLKIE001   
#General Allections sim
#Assignment 6, question 3
#22/04/14


votes = []      #stores users entered votes
candidates = [] #stores the unique candidates entered
numVotes = []   #stores the number of votes for each candidate


tempString = ""
currentWord = ""

print("Independent Electoral Commission")
print("--------------------------------")

 
tempString = input("Enter the names of parties (terminated by DONE):\n")

#fills votes list
while tempString != "DONE":
    votes.append(tempString)
    tempString = input("")
print("")
# sorts through votes lsit and stores uniques candidates in candidates list
for i in range(len(votes)):
    currentWord = votes[i]
    if currentWord in candidates:
        continue
    else:
        candidates.append(currentWord)
        numVotes.append(0)

candidates.sort()

# counts the number of votes per candidate
for i in range(len(candidates)):
    for j in range(len(votes)):
        if(candidates[i] == votes[j]):
            numVotes[i] = numVotes[i] + 1

# dictionary = dict(zip(candidates, numVotes))

out = "{0:<10}"
print("Vote counts:")

for i in range(len(candidates)):
    print(out.format(candidates[i]) + " - " + str(numVotes[i]))