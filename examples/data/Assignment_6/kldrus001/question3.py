#Rushil Kalidas
#Voting

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

vote_list= []
while True:
    x= input()
    if x=="DONE":break
    vote_list.append(x)
    
print()
print("Vote counts:")
parties = []
if vote_list != []:
    for i in vote_list:
        if i not in parties:
            parties.append(i)

parties.sort()

for j in parties:
    print("{0:<10}".format(j), "-", vote_list.count(j))