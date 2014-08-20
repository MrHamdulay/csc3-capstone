# assignment 6 question 3
import operator
print('''Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):''')
name = ""
names = []
votes = []
while name != "DONE":
    name = input()
    if name == "DONE":
        break
    if name not in names:
        names.append(name)
        votes.append(1)
    else:
        index = 0
        for i in names:
            if name == i:
                votes[index] += 1
            index += 1
for i in range(len(names)):
    names[i] = [names[i], votes[i]]
names = sorted(names,key=lambda x : x[0])
print("\nVote counts:")
for i in range(len(names)):
    print(names[i][0], " " * (10 - len(names[i][0])), " - ", names[i][1], sep = "")
