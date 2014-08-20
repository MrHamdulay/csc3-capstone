"""CSC1015F Assignment 6 Question 3
Xola Matlanyane MTLXOL002
25 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

parties = {}
elect = []
end = 0

while end == 0:
    vote=input("")
    if vote != "DONE":
        if vote not in parties:
            parties[vote] = 1
            elect.append(vote)
        else:
            parties[vote]+=1
    else:
        break
print("")
print("Vote counts:")
elect.sort()
for i in range(len(elect)):
    print("{0:11}- {1}".format(elect[i], parties[elect[i]]))
