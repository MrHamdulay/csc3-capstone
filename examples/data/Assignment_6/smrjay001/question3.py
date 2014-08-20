"""
Assignment 6 - Question 1
Program to count number of inputed items, i.e. votes
Jayan Smart
April 2014
"""

#Allow user to key in votes, end with DONE:
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
votes = []
while True:
    vote = input()
    if vote == 'DONE':
        break
    else:
        votes.append(vote)

#Create dictionary to count each votes occourance:
result ={}
result_alpha = []
for word in votes:
    if word not in result:
        result[word] = 0
        result_alpha.append(word)
    result[word] += 1
result_alpha.sort()

#Print results:
print("\nVote counts:")
for i in result_alpha:
    print(i+(" "*(11 - len(i)))+'- '+str(result[i]))
