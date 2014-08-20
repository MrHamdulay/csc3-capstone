"""Program to count votes
Tamsin Kantor
April 22 2014"""

# get votes

print("Independent Electoral Commission")
print("--------------------------------")
V = []
votes = input("Enter the names of parties (terminated by DONE):\n")
while votes != "DONE":
    V.append(votes)
    votes = input ()
    
# count votes and print vote counts

V.sort()
print()
print("Vote counts:")
for i in V:
    print("{0:<10}".format(i), " - ", V.count(i), sep="")
    for x in range(V.count(i)-1):
        V.remove(i)