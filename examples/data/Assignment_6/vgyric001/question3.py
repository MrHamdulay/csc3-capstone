#RICHARD VAN GYSEN
#23 APRIL 2014
#QUESTION 3
print("Independent Electoral Commission")
print("--------------------------------")
#GET PARTY NAMES
parties = input("Enter the names of parties (terminated by DONE):\n")
lis =[]
lis.sort()
#ADD TO LIST
while parties != "DONE":
    lis.append(parties)
    parties = input()
    lis.sort()
lis.sort()
counter = {}
#COUNT VOTES
for word in sorted(lis):
    if not word in counter:
        counter[word] = 1
    else:
        counter[word] += 1

print()
#PRINT VOTES FOR EACH PARTY
print("Vote counts:")
#for word in counter:
for word in sorted(counter):
    print (word,' '*(9-len(word)),"-",counter[word])   
