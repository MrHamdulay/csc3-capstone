#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     count votes for a list of parties
#
# Author:      Matthias
#
# Created:     20-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

parties = []
results = []

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
print("")

# get list of parties
while True:
    string = input("")
    if string == "DONE":
        break
    parties.append(string)

# count number of occurences and store as a two-dimensional array
for word in parties:
    i = 0
    # loop through list to check if word already exists in results
    while i < len(results):
        if results[i][0] == word:
            # update vote counter by one
            results[i][1] += 1
            break
        i += 1
    else:
        # if word is not yet in results, append it with one vote
        results.append([word,1])

results = sorted(results)

print("Vote counts:")

# print each party and its corresponding number of votes in a formatted way
for list in results:
    party = list[0]
    vote = list[1]
    print("{0:<10} - {1}".format(party,vote))