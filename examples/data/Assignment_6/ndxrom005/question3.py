

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

vote= [] #empty list
while True:
    x= input()
    if x=="DONE":break
    vote.append(x)
    
print()
print("Vote counts:")
parties = []
if vote != []: #ensure no syntax error
    for i in vote:
        if i not in parties:
            parties.append(i)

parties.sort()

for j in parties:
    print("{0:<10}".format(j), "-", vote.count(j))