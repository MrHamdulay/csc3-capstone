#Voting
#Sofia Palmer
#23 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
name = input("Enter the names of parties (terminated by DONE):\n")
names = []

#add each name to names list until DONE
while name != "DONE":
    names.append(name)
    name = input()

#create a dictionary for the party names and votes
parties = {}
#iterate through the input names and check whether they are in the dictionary thus far
for i in range(len(names)):
    unique = -1
    for x in parties:
        if (names[i] == x):
            parties[x] += 1
            unique = 0
            break
    if (unique == -1):
        parties[names[i]] = 1
      
#print party and votes
print()
print("Vote counts:")
lst = []
for k in parties:
    lst.append(k)

lst.sort()
for j in range(len(lst)):
    print("{0:<10}".format(lst[j]), "-",parties[lst[j]])
    
