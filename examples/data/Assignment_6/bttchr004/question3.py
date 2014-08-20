#program to count cotes
#chris betteridge
#21 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
votes = []
parties = []
names = input("Enter the names of parties (terminated by DONE):\n")
while names != "DONE":
    votes.append(names)
    names = input()
for i in votes:
    if i not in parties:
        parties.append(i)
print("\nVote counts:")
parties.sort()
for i in parties:
    votes.count(i)
    print(i,(11 - len(i))*" ","- ", votes.count(i),sep="")